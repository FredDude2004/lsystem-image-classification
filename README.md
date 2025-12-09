# L-System Image Classification

This project explores the intersection of formal language theory, procedural generation, and machine learning by using **Stochastic Lindenmayer Systems** to generate labeled training data for **Supervised Machine Learning** models. By leveraging the deterministic yet complex patterns of L-systems, we can automatically create large datasets of images that can be used to train AI models for classification tasks.

## Table of Contents

- [Installation and Use](#installation-and-use)
- [Lindenmayer Systems (L-Systems)](#lindenmayer-systems-l-systems)
- [Java L-System implementation ](https://github.com/FredDude2004/L-Systems)
- [Stochastic Lindenmayer Systems](#stochastic-lindenmayer-systems)
- [Supervised Machine Learning](#supervised-machine-learning)
- [Project Overview](#project-overview)
- [License](#license)

- [Image classification with Python and Scikit learn | Computer vision tutorial](https://www.youtube.com/watch?v=il8dMDlXrIE)

---

## Installation and Use

You need Python version 3.11 to run this so make sure that you have the correct version of Python installed. 

```bash
# clone the repo and move into it
git clone https://github.com/FredDude2004/lsystem-image-classification.git
cd lsystem-image-classification/src

# create a virtual environment, activate it and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Next you need to train the model by running the main.py

```bash
python main.py
```

Then you can run the client program predict.py and you can give it the path to any of the .jpg images that we placed in the src/ folder

```bash
python predict.py
```

## Lindenmayer Systems (L-Systems)

**Lindenmayer Systems**, commonly known as **L-systems**, are a formal grammar system developed by Hungarian theoretical biologist Aristid Lindenmayer in 1968. Originally designed to model the growth patterns of plants and organisms, L-systems have become a powerful tool in computer graphics, procedural generation, and algorithmic art.

### How L-Systems Work

An L-system consists of:

1. **Alphabet**: A set of symbols that can be used to create strings
2. **Axiom**: An initial string (starting point)
3. **Production Rules**: A set of rules that define how symbols are replaced in each iteration

### Example

Consider a simple L-system:

- **Alphabet**: `{A, B}`
- **Axiom**: `A`
- **Rules**:
  - `A → AB`
  - `B → A`

**Iterations**:
- Generation 0: `A`
- Generation 1: `AB`
- Generation 2: `ABA`
- Generation 3: `ABAAB`
- Generation 4: `ABAABABA`

### Applications

L-systems are particularly useful for:
- **Modeling plant growth** (branching structures, leaves, flowers)
- **Generating fractals** (Koch curve, Sierpinski triangle, dragon curve)
- **Creating procedural content** (terrain, vegetation in video games)
- **Simulating biological processes** (cell division, organism development)

The beauty of L-systems lies in their ability to generate complex, natural-looking structures from simple rules through recursive application.

---

## Stochastic Lindenmayer Systems

**Stochastic Lindenmayer Systems** extend traditional L-systems by introducing **randomness** into the production rules. Instead of having deterministic rules where each symbol always transforms the same way, stochastic L-systems use **probabilistic rules** that can produce different outcomes.

### Key Differences from Standard L-Systems

In a standard L-system, each symbol has exactly one production rule:
- `A → AB` (always happens)

In a stochastic L-system, each symbol can have multiple production rules, each with an associated probability:
- `A → AB` (70% probability)
- `A → A` (30% probability)

### Example

Consider a stochastic L-system:

- **Axiom**: `F`
- **Rules**:
  - `F → F[+F]F[-F]F` (60% probability)
  - `F → F[+F]F` (40% probability)

Each iteration will produce different results based on the random selection of rules according to their probabilities, leading to more natural and varied outcomes.

### Advantages for Data Generation

Stochastic L-systems are particularly valuable for machine learning applications because they can:

1. **Generate diverse datasets**: The randomness ensures that each generated structure is unique while maintaining underlying patterns
2. **Simulate natural variation**: Real-world objects (plants, trees, corals) show natural variation, which stochastic L-systems can replicate
3. **Create labeled data efficiently**: By controlling the rules and probabilities, we can generate different classes of structures with known labels
4. **Produce large training sets**: Automated generation can create thousands of unique examples without manual creation

---

## Supervised Machine Learning

**Supervised Machine Learning** is a type of machine learning where an algorithm learns from labeled training data to make predictions or classifications on new, unseen data. The term "supervised" comes from the idea that the algorithm is trained with the "correct answers" (labels) provided for each example.

### Key Concepts

#### 1. Training Data
Training data consists of **input-output pairs** where:
- **Input (Features)**: The data fed into the model (e.g., images, text, numbers)
- **Output (Labels)**: The correct answer or category for each input

#### 2. The Learning Process

The supervised learning process follows these steps:

1. **Data Collection**: Gather labeled examples
2. **Training**: The algorithm learns patterns by analyzing the relationship between inputs and their labels
3. **Validation**: Test the model on unseen data to evaluate its performance
4. **Prediction**: Use the trained model to make predictions on new data

#### 3. Types of Supervised Learning

- **Classification**: Predicting categorical labels (e.g., "Is this image a cat or a dog?", "Which plant species is this?")
- **Regression**: Predicting continuous values (e.g., "What is the temperature?", "What is the house price?")

### Common Algorithms

Popular supervised learning algorithms include:
- **Neural Networks / Deep Learning**: Powerful for complex patterns, especially in images and text
- **Decision Trees and Random Forests**: Interpretable models that work well with structured data
- **Support Vector Machines (SVM)**: Effective for high-dimensional data
- **K-Nearest Neighbors (KNN)**: Simple algorithm based on similarity
- **Logistic Regression**: Despite its name, used for classification tasks

### Challenges

- **Data Quality**: Models are only as good as the data they're trained on ("garbage in, garbage out")
- **Labeling Costs**: Creating labeled datasets can be expensive and time-consuming
- **Overfitting**: Models may memorize training data instead of learning generalizable patterns
- **Data Imbalance**: Unequal representation of classes can bias the model

---

## Project Overview

This project addresses one of the key challenges in supervised machine learning: **the cost and effort of generating large, labeled datasets**. 

### The Concept

By using **Stochastic Lindenmayer Systems**, we can:

1. **Define different L-system rules** that represent different categories or classes
2. **Generate thousands of unique structures** for each category automatically
3. **Render these structures as images** with known labels
4. **Train a supervised learning model** to classify images into their correct categories

### Advantages of This Approach

✅ **Automated Data Generation**: No manual labeling required  
✅ **Infinite Scalability**: Can generate as many training examples as needed  
✅ **Perfect Labels**: Each generated image is automatically labeled correctly  
✅ **Controlled Variation**: Can adjust stochasticity to control within-class variance  
✅ **Cost-Effective**: No need for expensive data collection or annotation services

### Potential Applications

This approach could be applied to:
- **Botanical classification**: Training models to identify plant species from their structures
- **Pattern recognition**: Learning to distinguish between different types of fractals or geometric patterns
- **Procedural content validation**: Verifying that generated game assets belong to intended categories
- **Educational tools**: Teaching machine learning concepts with easily generated, visualizable data

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
