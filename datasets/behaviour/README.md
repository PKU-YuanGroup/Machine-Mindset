## 数据集介绍 (Dataset Introduction)

以下是用于监督微调（SFT）的***行为数据集***，它们也可以用于直接偏好优化（DPO）。

Here are the ***behavior datasets*** used for supervised fine-tuning (SFT), which can also be utilized for direct preference optimization (DPO).

您可以在 [HuggingFace](https://huggingface.co/datasets/FarReelAILab/Machine_Mindset) 找到完全相同的副本。

An identical copy of these datasets can also be found on [HuggingFace](https://huggingface.co/datasets/FarReelAILab/Machine_Mindset).

'en' 目录包含了**英文版本**的数据集。

The 'en' directory contains datasets of the **English version**.

'zh' 目录包含了**中文版本**的数据集。

The 'zh' directory contains datasets of the **Chinese version**.

MBTI 具有四个维度，每个维度内有两个相对立的属性。

MBTI has four dimensions, each with two opposing attributes.

具体来说 (To be specific):

+ 能量 (Energe): 外向 (Extraversion, E) - 内向 (Introversion, I)

+ 信息 (Information): 感知 (Sensing, S) - 直觉 (Intuition, N)

+ 决策 (Decision): 思维 (Thinking, T) - 感觉 (Feeling, F)

+ 执行 (Execution): 判断 (Judging, J) - 感知 (Perceiving, P)

基于上述内容，您可以从文件名中推断出 JSON 文件的内容。

Based on the above, you can infer the content of the JSON file from its name.

这些数据集遵循 Alpaca 格式，包括指令、输入和输出。

The datasets follow the Alpaca format, consisting of instructions, input, and output.

如何使用这些数据集进行行为监督微调 (SFT) 和直接偏好优化 (DPO) 的详细说明：

Detailed instructions on how to use these datasets for supervised fine-tuning (SFT) and direct preference optimization (DPO):

### 行为监督微调 (SFT) (How to use these datasets for supervised fine-tuning)

例如，如果您想让一个 LLM 表现得像一个 ***ISFJ***，您需要选择 ***四个相应的文件*** (en_energe_introversion.json, en_information_sensing.json, en_decision_feeling.json, en_execution_judging.json)。

For example, if you want to make an LLM behave like an ***ISFJ***, you need to select ***the four corresponding files*** (en_energe_introversion.json, en_information_sensing.json, en_decision_feeling.json, en_execution_judging.json).

然后将这四个文件用于 SFT。

And use these four for SFT.

### 直接偏好优化 (DPO) (How to use these datasets for direct preference optimization)

例如，如果您想通过 DPO 让一个 LLM 表现得比思考（T）更 ***感性（F）***，您需要选择 ***两个相应的文件*** (en_decision_feeling.json, en_decision_thinking.json)。

For example, if you want to make an LLM be ***more feeling (F) than thinking (T)*** by DPO, you need to select ***the two corresponding files*** (en_decision_feeling.json, en_decision_thinking.json).

然后将这两个文件编译成正确的 DPO 格式。有关正确格式，请参考 [此链接](https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/datasets/dpo/README.md)。

And then compile these two into the correct format for DPO. For the correct format, please refer to [this link](https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/datasets/dpo/README.md).
