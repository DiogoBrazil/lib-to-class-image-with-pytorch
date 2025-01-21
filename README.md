# TorchImageClass

**TorchImageClass** é uma biblioteca em Python que fornece um conjunto de ferramentas e utilitários para **classificação de imagens** usando [PyTorch](https://pytorch.org/). Ela visa facilitar o **treinamento**, **validação** e **inferência** de redes neurais voltadas a tarefas de classificação.

---

## Sumário

- [Motivação](#motivação)
- [Principais Recursos](#principais-recursos)
- [Instalação](#instalação)

---

## Motivação

Modelos de classificação de imagens são amplamente usados em aplicações de visão computacional, desde identificação de objetos até detecção de doenças em exames de imagem. O **TorchImageClass** simplifica esse processo, fornecendo:

- **Arquiteturas** pré-definidas (ResNet, etc.) ou personalizáveis.  
- **Data loaders** e **transforms** para imagens.  
- **Treinamento** com otimização, métricas e *early stopping*.  
- **Práticas de *logging* e salvamento de modelos** (checkpoints).  
- **Inferência** em lote ou em imagens individuais.

---

## Principais Recursos

1. **Fácil inicialização de Modelos**  
   - Classes prontas para ResNet, VGG, etc., com poucas linhas de código.

2. **Treinamento Automatizado**  
   - Loop de treino e validação com métricas integradas (acurácia, precisão, recall).

3. **Data Augmentation Simplificada**  
   - Integração direta com `torchvision.transforms`.

4. **Suporte a GPU/CPU**  
   - Reconhecimento automático de dispositivo (CUDA/ROCm ou CPU).

5. **Exportação de Modelos**  
   - Salva pesos em formatos `.pth` ou `.pt`.

---

## Instalação

Para instalar via [PyPI](https://pypi.org/):

```bash
pip install TorchImageClass
