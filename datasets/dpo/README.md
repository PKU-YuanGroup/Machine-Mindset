## 直接偏好优化（DPO）文档介绍 (Direct Preference Optimization Documentation)

MBTI 具有四个维度，每个维度包含两个属性，因此天然地适用于直接偏好优化（DPO）。以下是一个更详细的介绍，以及如何使用我们提供的数据集来实现 DPO。

MBTI has four dimensions, each containing two attributes, making it a natural fit for Direct Preference Optimization (DPO). Below is a more detailed introduction and how to use the datasets we provide for DPO.

### 为什么选择 MBTI 数据集进行 DPO？ (Why Choose MBTI Datasets for DPO?)

MBTI 数据集的四个维度和属性的组合，为模型的偏好优化提供了丰富的可能性。以第一个维度 "能量" 为例，包括 "内向"（I）和 "外向"（E）两种属性。如果您希望模型更加内向而不是外向，您可以使用相应的 `zh_energy_introversion.json` 和 `zh_energy_extraversion.json` 数据文件，将它们组合成一个新的 DPO 类型的 JSON 数据集，例如 `dpo_energy_i_e.json`，从而获得更偏向内向而不是外向的数据集。这种方式适用于所有四个维度，提供了广泛的选择和实验可能性。

The combination of four dimensions and attributes in MBTI datasets provides a rich landscape for optimizing model preferences. Take the first dimension, "Energe," for example, which includes "Introversion" (I) and "Extraversion" (E) attributes. If you want your model to exhibit more introverted behavior rather than extraverted, you can use the corresponding `zh_energy_introversion.json` and `zh_energy_extraversion.json` data files and combine them into a new JSON dataset of DPO type, such as `dpo_energy_i_e.json`. This approach is applicable to all four dimensions, offering a wide range of choices and experimental possibilities.

### 如何进行 DPO 训练？ (How to Perform DPO Training?)

假设我们想对 INFP 模型进行 DPO 训练，以使其在 MBTI 四个维度上表现出特定的偏好。为了实现这一目标，我们需要获取四个数据集，分别代表 MBTI 的四个维度（能量、信息、决策和执行）。在这个示例中，我们需要以下四个数据集：

Let's assume we want to conduct DPO training on an INFP model to make it exhibit specific preferences across the four MBTI dimensions (Energe, Information, Decision, and Execution). In this example, we need four datasets representing these dimensions:

- `en_energe_introversion.json` (Energe dimension, Introversion attribute)
- `en_information_sensing.json` (Information dimension, Sensing attribute)
- `en_decision_feeling.json` (Decision dimension, Feeling attribute)
- `en_execution_perceiving.json` (Execution dimension, Perceiving attribute)

接下来，将这四个数据集组合在一起，并随机排列它们，以创建一个新的 DPO 数据集，例如 `dpo_infp.json`。这个新数据集将包含了来自不同维度的属性组合，帮助您实现对 INFP 模型的特定偏好优化。

Next, combine these four datasets and randomize them to create a new DPO dataset, such as `dpo_infp.json`. This new dataset will include attribute combinations from different dimensions, helping you achieve specific preference optimization for the INFP model.

### 多语言混合训练 (Multilingual Mixed Training)

请注意，您还可以进行多语言混合训练，这意味着您可以使用多种语言的数据集来训练模型。根据我们的实验结果，这种方法可以产生更好的效果，帮助您实现更丰富和多样化的模型行为。

Please note that you can also perform multilingual mixed training, which means you can use datasets in multiple languages to train your model. According to our experimental results, this approach can yield better outcomes and enable richer and more diverse model behaviors.

通过利用 MBTI 数据集进行 DPO 训练，您可以根据您的需求和目标，为模型的行为和性格定制特定的偏好，从而实现更加个性化的自然语言生成。

By leveraging MBTI datasets for DPO training, you can customize specific preferences for your model's behavior and personality based on your needs and goals, resulting in a more personalized natural language generation.
