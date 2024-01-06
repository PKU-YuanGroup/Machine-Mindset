<p align="center">
    <img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/logo.png" width="650" style="margin-bottom: 0.2;"/>
<p>
<h2 align="center"> <a href="https://arxiv.org/pdf/2312.12999.pdf">Machine Mindset: MBTI による大規模言語モデルの探求</a></h2>
<h5 align="center">もし私たちのプロジェクトを気に入っていただけたら、ぜひ星をつけてください⭐  </h2>


<h5 align="center">


[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/FarReelAILab/Machine_Mindset_zh_INTP)
[![arXiv](https://img.shields.io/badge/Arxiv-2312.12999-b31b1b.svg?logo=arXiv)](https://arxiv.org/pdf/2312.12999.pdf) 
[![Open in OpenXLab](https://cdn-static.openxlab.org.cn/header/openxlab_models.svg)](https://openxlab.org.cn/)
<br>
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


## 📰 ニュース

* **[2023.12.21]**  📑**私たちの arxiv は現在、探索のためにオープンになっています！** 最新の研究論文[こちら](https://arxiv.org/pdf/2312.12999.pdf)をご覧ください。
* **[2023.12.20]**  🤗[Hugging Face デモ](https://huggingface.co/FarReelAILab/Machine_Mindset_zh_INTP) **Machine-Mindset の Hugging Face demo と MBTI モデルの宝庫**の紹介！最先端のリソースを公開しますので、ご参加ください。最新のアップデートはこのリポジトリに👀をおいてください。

## 🚀 イントロダクション
**MM（Machine_Mindset）** シリーズのモデルは、FarReel AI Lab（旧 ChatLaw プロジェクト）と北京大学深層研究所のコラボレーションによって開発されました。これらのモデルは、Baichuan と LLaMA2 プラットフォーム上に構築された、中国語と英語の様々な MBTI タイプの大規模言語モデルになります。 🤖🌐

当社の中核となる資産は、数十万件からなる MBTI データセットです。当社のモデルは **事前訓練、微調整、DPO 訓練などの複数の段階を経て** 作成されています。私たちは、優れた性能を提供するためにモデルを継続的に更新することを約束し、実験的なテスト結果で常にモデルを補足していきます。 📊📈

単にプロンプトを使ってモデルの性格を変えるのとは対照的に、この方法は非常に不安定であることがわかりました。それは、内向的な子供に対して支配的な親が不満を抱き、単純で強圧的な命令によって強制的に外向的にさせようとするのに似ています。 🙅‍♂️😄

私たちは、Baichuan、Qwen、LLaMA、Mistral などのモデルを使用して、さまざまな MBTI タイプに対して**パーソナリティアライメント**を達成することに成功しています。つまり、異なるベースモデルを我々のデータセットとトレーニング方法と組み合わせ、各モデルを特定のタスクに合わせて調整することで、16 種類の MBTI 性格モデルを得ることができます。 🛠🧩

リソースの制約上、当初は Baichuan-7b-chat をベースにした16の中国語モデルと、LLaMA2-7b をベースにしたいくつかの英語モデルをリリースします。しかし、必要であれば、すぐに異なるバージョンのモデルを追加することができますので、ご安心ください。 🌍📦

これは、大規模言語モデル（LLM）をパーソナリティや心理学と組み合わせる私たちの最初の試みです。私たちは今後もこの方向性を探求していきます: 🚀🌱

MoE（専門家の混合）アーキテクチャを使用した MBTI モデルの実装
大規模言語モデルを使用したパーソナライズされたニーズへの対応
知的エージェントの計画タイプに関連する感情的な交友関係とタスクの探求。 🧠❤️
より深い理解、学術提携、投資、ビジネス提携に関するお問い合わせは、jiaxicui446@gmail.com。

## 🌟 エキサイティングなハイライト！ 🌟

私たちは、私たちの最新の製品を紹介することに興奮しています: 2 つではなく、**16 の MBTI モデル**が、あなたの探求のために利用可能になりました！私たちのオープンソースの宝庫で、パーソナリティの領域に深く飛び込んでみてください。

🤔 これらのモデルを使って何ができるのか不思議に思いませんか？エキサイティングな可能性をいくつかご紹介しましょう:

+ **特別な日に、パートナー** への完璧な贈り物を見つける。
+ **あなたがフォローしている個人** が様々な状況でどのような反応を示すかについての洞察を得る。
+ 大規模モデルのカスタマイズ、パーソナライズ、可能性について理解を深める。
+ 重要な決断を下す際には、さまざまな文脈における性格特性を考慮する。
+ 複雑な人間性を深く理解することで、個人の成長と相互理解を促進する。

LLM大規模モデルの時代に、かつてないほど性格タイプについての理解を深めよう！ 🎉🧠🌈

<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/arxiv_index.png" style="width=40%;"/></div>


## 🚀 主な結果

### ランダム質問と回答の結果
以下に、それぞれ独自の特徴や傾向を持つ性格タイプ別に、ランダム問答の結果を視覚的に示します:

+ **ENFP の結果** ENFP のパーソナリティの世界に飛び込み、ランダムな質問に対する彼らの回答を洞察する。その回答から、ENFP の創造的で想像力豊かな性格を発見してください。
<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/EN_ENFP_res.png" style="width=40%;"/></div>

+ **INTJ の結果** INTJ の性格の結果に飛び込み、ランダムな質問に取り組む分析的で戦略的なアプローチを観察する。INTJ がどのように様々なシナリオを正確かつ論理的にナビゲートするかについて洞察する。
<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/EN_INTJ_res.png" style="width=40%;"/></div>

+ **INFP の結果** INFP の性格の反応を発見し、無作為な質問に答えるときの彼らの理想主義的で共感的な性質を評価する。彼らのユニークな視点と洞察力を探ってみよう。
<div align="center"><img src="https://raw.githubusercontent.com/PKU-YuanGroup/Machine-Mindset/main/images/EN_INFP_res.png" style="width=40%;"/></div>

INTP の性格を調査し、無作為な質問に対する分析的で論理的なアプローチを観察する。問題解決能力や創造的思考能力についての洞察を得る。
これらの視覚的な表現は、性格タイプの多様な世界を垣間見せ、各タイプに関連するユニークな特徴や傾向をよりよく理解し、理解する機会を提供する。 📊🧠🔍




## 🔒 ライセンス

* 私たちのコードは Apache 2.0 のオープンソースライセンスに準拠しています。オープンソース規約の具体的な詳細については、[LICENSE](https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/LICENSE) を参照してください。

* 私たちのモデルウェイトは、オリジナルのウェイトに基づくオープンソース契約の対象であり、具体的な詳細は baichuan オープンソースライセンスの下、中国語版で提供されています。商用利用については、[model_LICENSE](https://huggingface.co/JessyTsu1/Machine_Mindset_zh_INTP/resolve/main/Machine_Mindset%E5%9F%BA%E4%BA%8Ebaichuan%E7%9A%84%E6%A8%A1%E5%9E%8B%E7%A4%BE%E5%8C%BA%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE.pdf) をご参照ください。

* 英語版は [llama2 license](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) のオープンソース契約に従っています。

## ✏️ 引用

もし私たちの論文やコードがあなたの研究に役立つとお感じになりましたら、Star :star: と引用 :pencil: をつけることをご検討ください。

```BibTeX
@misc{cui2023machine,
      title={Machine Mindset: An MBTI Exploration of Large Language Models}, 
      author={Jiaxi Cui and Liuzhenghao Lv and Jing Wen and Rongsheng Wang and Jing Tang and YongHong Tian and Li Yuan},
      year={2023},
      eprint={2312.12999},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```


<!---->

## ✨ Star History

[![Star History](https://api.star-history.com/svg?repos=PKU-YuanGroup/Machine-Mindset&type=Date)](https://star-history.com/#PKU-YuanGroup/Machine-Mindset&Date)

## 🤝 コントリビューター

<!-- readme: collaborators,contributors -start -->
<!-- readme: collaborators,contributors -end -->
