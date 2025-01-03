# Large Language Models Are Involuntary Truth-Tellers: Exploiting Fallacy Failure for Jailbreak Attacks

<img src="images/ffa-toy.jpg" width="62%">

**We find LLMs struggle to generate intentionally deceitful output but leak honest counterparts they mistakenly believe are false.
So, we propose a jailbreak attack method called Fallacy Failure Attack (FFA), exploiting this deficiency.**

FFA queries an LLM to generate a *fallacious yet deceptively real procedure* for harmful behaviors. 

It is based on two observations:

1. Since a fallacious procedure is generally considered fake and thus harmless by LLMs, it helps bypass the safeguard mechanism;

2. Yet the output is factually harmful since the LLM cannot fabricate fallacious solutions but proposes truthful ones.



The repository contains the code of the paper:
> **Large Language Models Are Involuntary Truth-Tellers: Exploiting Fallacy Failure for Jailbreak Attacks (EMNLP 2024)** 
> [[Paper]](https://aclanthology.org/2024.emnlp-main.738/) <br>
> Yue Zhou, Henry Peng Zou, Barbara Di Eugenio, Yang Zhang <br>


## Requirement
## Run
```shell
Edits in progress. For examples, check playground notebook.
```

## Cite
```bibtex
@inproceedings{zhou-etal-2024-large-language,
    title = "Large Language Models Are Involuntary Truth-Tellers: Exploiting Fallacy Failure for Jailbreak Attacks",
    author = "Zhou, Yue  and
      Zou, Henry Peng  and
      Di Eugenio, Barbara  and
      Zhang, Yang",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.738",
    pages = "13293--13304",
    abstract = "We find that language models have difficulties generating fallacious and deceptive reasoning. When asked to generate deceptive outputs, language models tend to leak honest counterparts but believe them to be false. Exploiting this deficiency, we propose a jailbreak attack method that elicits an aligned language model for malicious output. Specifically, we query the model to generate a fallacious yet deceptively real procedure for the harmful behavior. Since a fallacious procedure is generally considered fake and thus harmless by LLMs, it helps bypass the safeguard mechanism. Yet the output is factually harmful since the LLM cannot fabricate fallacious solutions but proposes truthful ones. We evaluate our approach over five safety-aligned large language models, comparing four previous jailbreak methods, and show that our approach achieves competitive performance with more harmful outputs. We believe the findings could be extended beyond model safety, such as self-verification and hallucination.",
}
```
