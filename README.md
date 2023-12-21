<p align="center">
    <img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/logo.png" width="650" style="margin-bottom: 0.2;"/>
<p>
<h2 align="center"> <a href="https://arxiv.org/pdf/2312.12999.pdf">Machine Mindset: An MBTI Exploration of Large Language Models</a></h2>
<h5 align="center"> 如果你喜欢我们的项目，请点赞 ⭐ 
<h4 align="center"> [ 中文 | <a href="https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/README_en.md">English]
</h2>



<h5 align="center">



[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/FarReelAILab/Machine_Mindset_zh_INTP)
[![arXiv](https://img.shields.io/badge/Arxiv-2312.12999-b31b1b.svg?logo=arXiv)](https://arxiv.org/pdf/2312.12999.pdf) <br>
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/LICENSE) 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FPKU-YuanGroup%2FMachine-Mindset&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Visitor&edge_flat=false)](https://hits.seeyoufarm.com)
      <a href="https://github.com/PKU-YuanGroup/Machine-Mindset/graphs/contributors">
        <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/PKU-YuanGroup/Machine-Mindset" />
      </a>
      <a href="https://github.com/PKU-YuanGroup/Machine-Mindset/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/PKU-YuanGroup/Machine-Mindset?color=0088ff" />
      </a>
      <a href="https://github.com/PKU-YuanGroup/Machine-Mindset/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/PKU-YuanGroup/Machine-Mindset?color=0088ff" />
      </a>
      <a href="https://github.com/PKU-YuanGroup/Machine-Mindset/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/PKU-YuanGroup/Machine-Mindset?color=ccf" />
      </a>
<br>

</h5>

## 📰 新闻

* **[2023.12.21]**  📑**Arxiv论文已开放!** 论文链接在 [此处](https://arxiv.org/pdf/2312.12999.pdf)。
* **[2023.12.20]**  🤗[Hugging Face 模型示例](https://huggingface.co/FarReelAILab/Machine_Mindset_zh_INTP) 我们在Hugging Face中开放了MBTI系列模型。


## 🚀 简介 

**MM(Machine_Mindset)** 系列模型是FarReel AI Lab和北大深研院合作研发的，基于Baichuan和LLaMA2的各种不同MBTI类型的中英文大语言模型。 🤖🌐

我们的核心资产是自主构建的数十万条大规模MBTI数据集，我们的模型**通过多阶段的预训练、微调和DPO训练** 而成。我们将不断更新模型，以提供更出色的性能，并持续补充实验测试结果。 📊📈

与简单地使用提示（prompt）来改变模型性格的方式相比，我们发现**prompt尝试改变性格的方式非常不稳定**，就像是**控制欲很强的父母对一个内向的孩子不满意，试图通过简单而强制性的命令来要求他变得外向一样荒谬**。 🙅‍♂️😄

我们成功地使用Baichuan、Qwen、LLaMA、Mistral等模型完成了不同MBTI类型的**性格对齐**任务，这意味着我们可以用不同的基座模型结合我们的数据集与训练方式，获得16个不同MBTI性格版本的模型，以使每个模型更适合不同的任务。 🛠🧩

鉴于资源有限，我们首先开放基于Baichuan-7b-chat的16个中文模型以及基于LLaMA2-7b的数个英文模型。但请放心，如果需要，我们可以迅速补充不同版本的模型。 🌍📦

这是我们将大型语言模型（LLM）与性格和心理学相结合的首次尝试，我们将继续在这个方向上进行探索，包括但不限于： 🚀🌱

- 采用MoE（Mixture of Experts）架构的MBTI模型
- 大型语言模型的个性化需求
- 情感陪伴以及与智能代理任务规划类型相关的任务。 🧠❤️

如果您有深入了解、进行学术合作、投资、商务合作的需求，请联系[jiaxicui446@gmail.com](mailto:jiaxicui446@gmail.com)


## 🌟 亮点 🌟

我们非常高兴向您介绍我们的最新产品：**不是两个，而是16个不同的MBTI模型**，现在可供您探索！深入人格领域，发掘我们的开源宝库。

🤔 想知道如何利用这些模型吗？以下是一些可能还不错的选项：

+ 在特殊节日，**给你的男/女朋友寻找心仪的礼物** 。
+ 了解 **你关注的那个Ta** 在不同情境下的反应。
+ 深入理解大模型的定制化、个性化的方式及可能性。
+ 在做出重大决策时，考虑不同情境下的个性特征。
+ 通过深入了解人性的复杂性，促进个人成长和相互理解。

来吧，在LLM大模型时代，以前所未有的方式深化您对人格类型的理解！ 🎉🧠🌈

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/index.png" style="width=40%;"/></div>


## 🚀 成果

### 问答

在下面，我们简单测试了几个不同人格类型的随机问答，每种类型都有其独特的特征和倾向：

+ **ENFP 问答结果** 深入探索ENFP人格类型的世界，了解他们的反应。来感受专属于ENFP独特的创造力和想象力。

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/ENFP_res.png" style="width=40%;"/></div>

+ **ENTJ 问答结果** 深入了解ENTJ人格类型的成果，留意他们在回答问题时所展现出的自信和策略性。了解他们如何应对各种情况。

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/ENTJ_res.png" style="width=40%;"/></div>

+ **ESTJ 问答结果** 深入了解ESTJ人格类型的回应，揭示他们面对问题时的有组织性和实用心态。探索他们逻辑性和高效的解决问题能力。

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/ESTJ_res.png" style="width=40%;"/></div>

+ **INFJ 问答结果** 探索INFJ人格类型的结果，并了解他们在回答问题时所表现出的同理心和内省方式。理解INFJ如何处理各种问题和情境。

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/INFJ_res.png" style="width=40%;"/></div>

+ **INFP 问答结果** 探索INFP人格类型的回应，并欣赏他们在回答问题时的理想主义和同理心。探索他们独特的观点和洞察力。

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/INFP_res.png" style="width=40%;"/></div>

+ **INTP 问答结果** 调查INTP人格类型的结果，并观察他们在处理随机问题时的分析和逻辑方法。了解他们在解决问题和创造性思维方面的能力。

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/INTP_res.png" style="width=40%;"/></div>

上述结果为我们提供了一个窥视多样化人格类型世界的机会，帮助我们更好地理解和欣赏与每种类型相关联的独特特质和倾向。 📊🧠🔍




## 🔒 许可

* 我们的代码遵循 Apache 2.0 开源许可. 请参照 [LICENSE](https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/LICENSE) 以获取细节。

* 我们的模型权重遵循基于原始权重的开源协议，具体细节在baichuan开源许可证下的中文版本中提供。 关于商用, 请参照 [model_LICENSE](https://huggingface.co/JessyTsu1/Machine_Mindset_zh_INTP/resolve/main/Machine_Mindset%E5%9F%BA%E4%BA%8Ebaichuan%E7%9A%84%E6%A8%A1%E5%9E%8B%E7%A4%BE%E5%8C%BA%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE.pdf) 以获取更多信息。

* 英文版本的模型遵循此开源许可 [llama2 license](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).

## ✏️ Citation

如果您在自己的研究中，发现我们的模型和代码有帮助, 请考虑点赞 :star: 并引用 :pencil:.

```BibTeX
@misc{cui2023machine,
      title={Machine Mindset: An MBTI Exploration of Large Language Models}, 
      author={Jiaxi Cui and Liuzhenghao Lv and Jing Wen and Jing Tang and YongHong Tian and Li Yuan},
      year={2023},
      eprint={2312.12999},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


<!---->

## ✨ Star History

[![Star History](https://api.star-history.com/svg?repos=PKU-YuanGroup/Machine-Mindset&type=Date)](https://star-history.com/#PKU-YuanGroup/Machine-Mindset&Date)

## 🤝 Contributors

<a href="https://github.com/PKU-YuanGroup/Machine-Mindset/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PKU-YuanGroup/Machine-Mindset" />
</a>
