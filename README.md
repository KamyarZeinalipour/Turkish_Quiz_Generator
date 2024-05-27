# Turkish_Quiz_Gen


[[`Paper`](paper_link)] [[`Turkish-Quiz-Instruct Dataset`](https://huggingface.co/datasets/Kamyar-zeinalipour/Turkish-Quiz-Instruct)] [[`BibTeX`](#citing-a-turkish-educational-quiz-generator)] 


Code Completion Generation using Pre-trained Models
=====================================================

This repository contains a Python script that generates code completions using pre-trained models. The script takes an input file containing prompts, generates code completions using a pre-trained model, and saves the output to a specified file.

Getting Started
---------------

### Prerequisites

* `Python 3.7` or later
* `PyTorch 1.9` or later
* Transformers library (install with `pip install transformers`)
* PEFT library (install with `pip install peft`)

### Installation

1. Clone this repository: `git clone https://github.com/your-username/code-completion-generation.git`
2. Install the required libraries: `pip install -r requirements.txt`

### Usage

1. Prepare an input file containing prompts in a CSV format with a single column named "text".
2. Run the script using the following command:
```
python quiz_gen_main.py --model_path <path-to-pre-trained-model> --input_file <input-file.csv> --output_file <output-file.csv> --temperature <temperature-value>
```
Replace `<path-to-pre-trained-model>` with the path to your pre-trained model, `<input-file.csv>` with the path to your input file, `<output-file.csv>` with the desired output file path, and `<temperature-value>` with the desired temperature value (default is 0.2).

### Example
```
python main.py --model_path /path/to/model --input_file input.csv --output_file output.csv --temperature 0.5
```

This will generate code completions for the prompts in `input.csv` using the pre-trained model at `/path/to/model` and save the output to `output.csv` with a temperature value of 0.5.

### Output

The script will generate a CSV file with two columns: "prompt" and "output". The "prompt" column contains the original prompts, and the "output" column contains the generated code completions.

### Troubleshooting

If you encounter any issues or errors, please check the console output for error messages or raise an issue on this repository.

License
-------

This project is licensed under the MIT License. See [MIT License](LICENSE) for details.

Contributing
------------

A Turkish Educational Quiz Generator paper was made possible with the help of many contributors (alphabetical):

Kamyar Zeinalipour, Leonardo Rigutini, Marco Gori, Marco Maggini, Yusuf Gökberk Keptiğ

Citing A Turkish Educational Quiz Generator
------------

```
@misc{zeinalipour2024turkish,
      title={A Turkish Educational Crossword Puzzle Generator}, 
      author={Kamyar Zeinalipour and Yusuf Gökberk Keptiğ and Marco Maggini and Leonardo Rigutini and Marco Gori},
      year={2024},
      eprint={2405.07035},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
Acknowledgments
---------------

This project uses the following libraries:

* Transformers: https://github.com/huggingface/transformers
* PEFT: https://github.com/huggingface/peft

Please cite the original authors of these libraries if you use this code in your research or projects.
