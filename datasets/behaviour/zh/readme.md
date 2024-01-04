## Dataset introduction

There are four dimension in MBTI. And there are two opposite attributes within each dimension.

To be specific:

+ Energe: Extraversion (E) - Introversion (I)

+ Information: Sensing (S) - Intuition (N)

+ Decision: Thinking (T) - Feeling (F)

+ Execution: Judging (J) - Perceiving (P)

Based on the above, you can infer the content of the json file from its name.

The datasets follow the Alpaca format, consisting of instruction, input and output.

## How to use these datasets for behavior supervised fine-tuning (SFT)

For example, if you want to make an LLM behave like an ***ISFJ***, you need to select ***the four corresponding files*** (zh_energe_introversion.json, zh_information_sensing.json, zh_decision_feeling.json, zh_execution_judging.json). 

And use the four for SFT.

## How to use these datasets for direct preference optimization (DPO)

For example, if you want to make an LLM be ***more feeling (F) than thinking (T)*** by DPO, you need to select ***the two corresponding files*** (zh_decision_feeling.json, zh_decision_thinking.json). 

And then compile the two into the correct format for DPO. For the correct format, please refer to [this](https://github.com/hiyouga/LLaMA-Factory/blob/main/data/comparison_gpt4_data_zh.json).

