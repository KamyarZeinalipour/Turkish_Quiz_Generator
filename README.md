# Automating Turkish Educational Quiz Generation Using Large Language Models

[![Paper](https://img.shields.io/badge/ISPR_2024-paper-b31b1b)](https://arxiv.org/abs/2406.03397)
[![Dataset](https://img.shields.io/badge/%F0%9F%A4%97_Dataset-Turkish--Quiz--Instruct-yellow)](https://huggingface.co/datasets/Kamyar-zeinalipour/Turkish-Quiz-Instruct)
[![Models](https://img.shields.io/badge/%F0%9F%A4%97_Collection-4_models-orange)](https://huggingface.co/collections/Kamyar-zeinalipour/turkish-educational-quiz-generation-ispr-2024-6af4852f9293af6e63c1acda)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Generate educational quiz questions in Turkish from any Turkish text. Given a passage, the models
write **multiple-choice** or **short-answer** questions for it. They were fine-tuned on
**Turkish-Quiz-Instruct**, 4,023 Turkish educational texts paired with generated questions across
school subjects.

This repository accompanies the paper
[*Automating Turkish Educational Quiz Generation Using Large Language Models*](https://arxiv.org/abs/2406.03397)
(ISPR 2024). Everything is collected in the
[Turkish Educational Quiz Generation collection](https://huggingface.co/collections/Kamyar-zeinalipour/turkish-educational-quiz-generation-ispr-2024-6af4852f9293af6e63c1acda).

## Models

| Task | Model | Adapter |
|---|---|---|
| Multiple-choice | Llama-2-7b-chat | [TR_QUIZ_GEN_MULTI_LLAMA7B](https://huggingface.co/Kamyar-zeinalipour/TR_QUIZ_GEN_MULTI_LLAMA7B) |
| Multiple-choice | Llama-2-13b-chat | [TR_QUIZ_GEN_MULTI_LLAMA13B](https://huggingface.co/Kamyar-zeinalipour/TR_QUIZ_GEN_MULTI_LLAMA13B) |
| Short-answer | Llama-2-7b-chat | [TR_QUIZ_GEN_SIMPLE_LLAMA7B](https://huggingface.co/Kamyar-zeinalipour/TR_QUIZ_GEN_SIMPLE_LLAMA7B) |
| Short-answer | Llama-2-13b-chat | [TR_QUIZ_GEN_SIMPLE_LLAMA13B](https://huggingface.co/Kamyar-zeinalipour/TR_QUIZ_GEN_SIMPLE_LLAMA13B) |

## Results

**Multiple-choice questions** (ROUGE-1 / ROUGE-2 / ROUGE-L, base → fine-tuned):

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|
| Llama-2-7b-chat | 4.71 → **17.33** | 1.42 → **2.88** | 3.88 → **12.11** |
| Llama-2-13b-chat | 5.33 → **24.34** | 1.73 → **11.44** | 4.28 → **19.75** |
| GPT-3.5-Turbo | 27.53 → **36.64** | 13.18 → **20.36** | 21.38 → **28.82** |

**Short-answer questions**:

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|
| Llama-2-7b-chat | 3.31 → **54.37** | 1.04 → **47.33** | 2.86 → **49.01** |
| Llama-2-13b-chat | 3.81 → **52.99** | 1.33 → **46.88** | 3.22 → **49.54** |
| GPT-3.5-Turbo | 28.19 → **45.31** | 15.87 → **31.59** | 22.22 → **40.32** |

Human evaluation by native Turkish speakers is reported in the paper.

## Installation

```bash
git clone https://github.com/KamyarZeinalipour/Turkish_Quiz_Generator.git
cd Turkish_Quiz_Generator
pip install torch transformers peft pandas
huggingface-cli login   # the Llama 2 base models are gated
```

Python 3.7+ and a CUDA GPU are recommended.

## Usage

Prepare a CSV with a single column named `text`, containing the Turkish passages:

```bash
python quiz_gen_main.py \
  --model_path Kamyar-zeinalipour/TR_QUIZ_GEN_MULTI_LLAMA7B \
  --input_file input.csv \
  --output_file output.csv \
  --temperature 0.2
```

| Argument | Description |
|---|---|
| `--model_path` | Model to use: one of the four above, or a local path |
| `--input_file` | Input CSV with a `text` column |
| `--output_file` | Where to write the results |
| `--temperature` | Sampling temperature (default `0.2`) |

The output CSV has two columns: `prompt` (the input passage) and `output` (the generated
questions).

## Dataset

[Turkish-Quiz-Instruct](https://huggingface.co/datasets/Kamyar-zeinalipour/Turkish-Quiz-Instruct):
4,023 rows with `content` (the Turkish text), `multiple_questions`, `short_questions`, `subject`
and `subsubtopic`.

## Contributors

Kamyar Zeinalipour, Marco Gori, Marco Maggini, Yusuf Gökberk Keptiğ

## Citation

```
@misc{zeinalipour2024automating,
      title={Automating Turkish Educational Quiz Generation Using Large Language Models}, 
      author={Kamyar Zeinalipour and Yusuf Gökberk Keptiğ and Marco Maggini and Marco Gori},
      year={2024},
      eprint={2406.03397},
      archivePrefix={arXiv},
      primaryClass={id='cs.CL' full_name='Computation and Language' is_active=True alt_name='cmp-lg' in_archive='cs' is_general=False description='Covers natural language processing. Roughly includes material in ACM Subject Class I.2.7. Note that work on artificial languages (programming languages, logics, formal systems) that does not explicitly address natural-language issues broadly construed (natural-language processing, computational linguistics, speech, text retrieval, etc.) is not appropriate for this area.'}
}
```
Acknowledgments
---------------

This project uses the following libraries:

* Transformers: https://github.com/huggingface/transformers
* PEFT: https://github.com/huggingface/peft

Please cite the original authors of these libraries if you use this code in your research or projects.

## License

MIT, see [LICENSE](LICENSE). The models follow the Llama 2 Community License.
