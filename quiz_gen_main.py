import argparse
import time
import pandas as pd
import torch
from transformers import AutoTokenizer
from peft import AutoPeftModelForCausalLM

# Constants
MAX_NEW_TOKENS = 128
TOP_K = 50
TOP_P = 0.95
NO_REPEAT_NGRAM_SIZE = 4
REPETITION_PENALTY = 1.0

def get_code_completion(prompt: str, model, tokenizer, temperature: float) -> str:
    """Generate code completion for a given prompt"""
    try:
        model.eval()
        outputs = model.generate(
            input_ids=tokenizer(prompt, return_tensors="pt").input_ids.cuda(),
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=temperature,
            top_k=TOP_K,
            top_p=TOP_P,
            do_sample=True,
            no_repeat_ngram_size=NO_REPEAT_NGRAM_SIZE,
            repetition_penalty=REPETITION_PENALTY,
        )
        return tokenizer.batch_decode(outputs, skip_special_tokens=False)[0]
    except Exception as e:
        print(f"Error during code generation: {e}")
        raise

def load_model(model_path: str) -> tuple:
    """Load the pre-trained model and tokenizer"""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoPeftModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16)
    model.cuda()
    return model, tokenizer

def process_input_file(input_file: str) -> pd.DataFrame:
    """Read the input file and return a pandas DataFrame"""
    return pd.read_csv(input_file)

def generate_code_completions(
    model, tokenizer, input_file: str, output_file: str, temperature: float
) -> None:
    """Generate code completions for the input file and save to the output file"""
    df = process_input_file(input_file)
    processed_df = pd.DataFrame(columns=["prompt", "output"])

    try:
        processed_df = pd.read_csv(output_file, sep="\t")
        last_index = processed_df.index[-1] if not processed_df.empty else -1
    except (FileNotFoundError, pd.errors.EmptyDataError):
        last_index = -1

    for i, row in df.iterrows():
        if i <= last_index:
            continue

        print("Row Number:", i)
        prompt = row["text"]
        try:
            response = get_code_completion(prompt, model, tokenizer, temperature)
            print(f"Traversing index at: {i}")
            print(response)

            processed_df = processed_df.append({"prompt": prompt, "output": response}, ignore_index=True)

            if i % 10 == 0:
                processed_df.to_csv(output_file, sep="\t", index=False)

        except Exception as e:
            print(f"Error encountered at row {i}: {e}. Waiting 2 minutes before retrying...")
            time.sleep(120)

    processed_df.to_csv(output_file, sep="\t", index=False)
    print("Generation complete.")

def main() -> None:
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Generate code completions using a pre-trained model.")
    parser.add_argument("--model_path", type=str, help="Path to the pre-trained model")
    parser.add_argument("--input_file", type=str, help="Path to the input file containing prompts")
    parser.add_argument("--output_file", type=str, help="Path to save the output file")
    parser.add_argument("--temperature", type=float, default=0.2, help="Temperature for generation")
    args = parser.parse_args()

    model, tokenizer = load_model(args.model_path)
    generate_code_completions(model, tokenizer, args.input_file, args.output_file, args.temperature)

if __name__ == "__main__":
    main()