# 🤖 AI for Decision Support – Exam Report

This repository documents the work done for the *Artificial Intelligence for Decision Support* course and for *Knowledge representation and computational logic* course. The first course explored core AI concepts with a focus on early AI algorithms from the 60s/70s, decision theory, and probabilistic reasoning. All algorithms and tools were implemented and tested using **Python**, with particular emphasis on **Bayesian Networks** using the **Genie** toolkit. The second course provides a solid foundation in logic-based knowledge representation and automated reasoning, emphasizing the semantics, expressiveness, and computational properties of various declarative formalisms.

---

## 🎯 Courses Mission

The course aimed to introduce the fundamental principles and goals of intelligent agents based on modern AI perspectives. Students developed the ability to:

- Understand algorithmic methods for state-space problem solving
- Model and solve problems using **case-based reasoning** systems
- Apply reasoning under uncertainty in knowledge-based systems
- Model and analyze decision problems using **probabilistic graphical models**
- Apply **decision theory** and **multi-attribute utility theory**
- Extend probabilistic models to **decision networks** for both one-shot and sequential decision-making
- Use dedicated tools (e.g., Genie) for decision analysis
- Develop critical thinking to choose the appropriate representation and inference strategies for intelligent systems

---

## 🧠 Topics Covered

### 📌 General AI Concepts
- Historical background of AI
- Blind and heuristic search (e.g., A*)
- Iterative improvement algorithms: Hill-Climbing and Simulated Annealing
- Constraint Satisfaction Problems (CSP) – basics
- Game theory algorithms: **Minimax** and **Alpha-Beta Pruning**

### 📌 Knowledge Representation & Logic-Based Reasoning
- Representation of knowledge using logical formulas and rules
- **Logic Programming** and **Constraint Logic Programming**
- **Answer Set Programming (ASP)** for declarative problem solving
- Use of logic-based tools for high-level reasoning
- **Description Logics** for structured knowledge domains
- **Temporal Logics** for reasoning over time-dependent events and conditions

These methods enabled a declarative approach to problem-solving, allowing the modeling of complex domains where knowledge evolves over time or is defined by strict logical rules.

### 📌 Knowledge-Based Systems
- Introduction to **Case-Based Reasoning (CBR)**
- Design of systems that reason by analogy using past experiences

### 📌 Uncertain Knowledge
- Basics of probability theory
- **Bayesian Networks**: Properties, algorithms, and implementation
- Use of Bayesian tools: **Genie**, **Hugin**

### 📌 Intelligent Decision Support Systems
- **Decision theory** and decision-making under uncertainty
- **Multi-attribute utility theory**
- **Influence diagrams**
- **One-shot and sequential decisions**

---

## 💡 Practical Implementation Highlights

During the course, I implemented and experimented with several AI algorithms and decision support tools, including:

- ✅ **A\***: Heuristic path-finding algorithm
- ✅ **Minimax**: Game-tree algorithm for two-player games
- ✅ **Likelihood Weighting**: Probabilistic sampling technique for approximate inference in Bayesian Networks

---

## 🧪 Bayesian Networks – Project Work

The project portion of the exam focused on **Bayesian reasoning and decision support**, divided into two exercises:

### 1. 📄 **Network Modeling from Text**
Given a textual description of a scenario, I designed a **Bayesian Belief Network** to represent dependencies among variables.

### 2. 🔗 **Python Integration with Genie**
Using **Genie’s API**, I connected the Bayesian Network to a Python script in order to:
- Query conditional probabilities
- Update beliefs based on user input
- Support decision-making based on real-time observations
