from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="TorchImageClass",
    version="0.0.1",
    author="Diogo Ribeiro",
    author_email="diogoifroads@gmail.com",
    description="A library for image classification using PyTorch.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    license="MIT",
    keywords=[
        "pytorch",
        "deep-learning",
        "image-classification",
        "machine-learning",
        "computer-vision",
        "classification",
        "torch",
        "TorchImageClass",
        "neural-networks",
        "cnn",
        "transfer-learning"
    ],
    install_requires=[
        "torch>=1.10",
        "torchvision>=0.11",
        "torchmetrics>=0.6",
        "tqdm>=4.0",
        "Pillow>=7.0",
    ],
    python_requires=">=3.9",
)
