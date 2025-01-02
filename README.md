# Hadoop and Spark Exercise - Phase 0 & Phase 1

This repository contains the implementation of the third assignment focusing on **Hadoop** and **Spark**, covering both **Phase 0** and **Phase 1**.

## Table of Contents
- [Introduction](#introduction)
- [Phase 0](#phase-0)
  - [Setup Instructions](#setup-instructions)
  - [Hadoop Components Overview](#hadoop-components-overview)
  - [Cluster Resources](#cluster-resources)
  - [Accessing UIs](#accessing-uis)
- [Phase 1](#phase-1)
  - [MapReduce Word Count](#mapreduce-word-count)
    - [Mapper Code](#mapper-code)
    - [Reducer Code](#reducer-code)
  - [Frequent Word Count](#frequent-word-count)
    - [Mapper Code](#mapper-code-1)
    - [Reducer Code](#reducer-code-1)
- [Execution Commands](#execution-commands)
- [Results](#results)
  - [Word Count Output](#word-count-output)
  - [Frequent Word Count Output](#frequent-word-count-output)
- [Bonus Task](#bonus-task)
- [Author](#author)

---

## Introduction
This project demonstrates distributed data processing using **Hadoop** and **Spark**. It includes containerized setup, exploration of Hadoop components, and MapReduce-based processing to implement word counting and frequent word identification tasks.

---

## Phase 0

### Setup Instructions
Follow the steps below to set up your environment:
1. Clone the repository:
   ```bash
   git clone git@github.com:sadegh-msm/hind.git
   ```
   For `arm64` architecture:
   ```bash
   git clone -b arm64 git@github.com:sadegh-msm/hind.git
   ```
2. Build the master container:
   ```bash
   bash master-build.sh
   ```
3. If needed, delete the existing cluster:
   ```bash
   bash master-delete.sh
   ```

### Hadoop Components Overview
The Hadoop cluster is composed of the following containers:
- **NameNode**: The central node in HDFS that manages the file system metadata.
- **DataNode**: Stores data blocks and serves read/write requests.
- **ResourceManager**: Allocates cluster resources in the YARN framework.
- **NodeManager**: Monitors resource usage on individual nodes.
- **Spark Master**: Coordinates task distribution in Spark clusters.
- **Spark Worker**: Executes tasks assigned by the Spark Master.
- **Jupyter Notebook**: Provides an interactive environment for live coding and data visualization.

### Cluster Resources
- **Number of Nodes**:
  - 1 Spark Master
  - 2 Spark Workers
- **Resource Allocation**:
  - 2 CPU cores per worker
  - 1024 MB RAM per worker
- **HDFS Details**:
  - Total Blocks: 83
  - Block Replication: 3
  - Storage Type: Disk (58.82 GB capacity)

### Accessing UIs
Access the cluster interfaces using the URLs below:
- Hadoop UI: [http://localhost:9870](http://localhost:9870)
- Spark Master UI: [http://localhost:8080](http://localhost:8080)
- Jupyter UI: [http://localhost:8888](http://localhost:8888)

---

## Phase 1

### MapReduce Word Count

#### Mapper Code
The mapper reads the input file line by line, splits words, and emits `word-document ID` pairs. Whitespace is removed, and the output is formatted for the reducer.

#### Reducer Code
The reducer aggregates all document IDs for each word, removes duplicates, and outputs a list of unique document IDs associated with every word.

### Frequent Word Count

#### Mapper Code
The mapper processes the input file similarly but focuses on counting occurrences for frequency analysis.

#### Reducer Code
The reducer uses a counter to identify the top `k=3` most frequent words. It outputs words along with their frequencies.

---

## Execution Commands
To run the project, execute the steps below:

1. **Upload Input File to HDFS**:
   ```bash
   hdfs dfs -put input.txt /user/hadoop/input
   ```

2. **Run MapReduce Job**:
   Use the following command to execute the MapReduce job:
   ```bash
   hadoop jar /opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
       -file mapper.py -mapper mapper.py \
       -file reducer.py -reducer reducer.py \
       -input input/input.txt -output output
   ```

3. **View Results**:
   Retrieve the results using:
   ```bash
   hdfs dfs -cat /user/hadoop/output/part-00000
   ```

---

## Results

### Word Count Output
Example:
```plaintext
apple    doc1, doc3
banana   doc1, doc2
orange   doc1, doc2, doc4
```

### Frequent Word Count Output
Example (`k=3`):
```plaintext
mango       5
apple       4
banana      3
```

---

## Bonus Task
The bonus task extends the frequent word count program to identify the top `k=3` most frequent words across multiple documents. 

Input Example:
```plaintext
doc1,apple apple apple banana banana orange mango mango mango
doc2,technology technology data data science machine learning
```

Output Example:
```plaintext
mango        5
technology   4
apple        3
```

---

## Author
**Mohammad Hosein**

For further questions or feedback, feel free to reach out.
