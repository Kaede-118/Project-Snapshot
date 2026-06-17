# Project-Snapshot

A lightweight project snapshot generator designed for AI code analysis.

Generate a directory tree and source code snapshot of a project, then export everything into a single text file for ChatGPT, Claude, Gemini, DeepSeek, and other LLMs.

---

# 中文

## 简介

Project-Snapshot 是一个轻量级项目快照工具。

它会自动扫描项目目录，生成目录树，并提取源码内容，最终导出为单个文本文件。

设计目标：

> 用最简单的方式，把一个项目变成 AI 能快速理解的单文件快照。

适用于：

* ChatGPT
* Claude
* Gemini
* DeepSeek
* 豆包
* 其他支持文件上传的大语言模型

---

## 功能

* 项目目录树导出
* 自动收集源码文件
* 自动过滤常见编译产物和二进制文件
* 自动过滤 `.git`、`target`、`node_modules` 等目录
* 大文件自动跳过
* 长文件自动截断
* FULL 模式完整导出
* 单文件输出，方便提交给 AI 分析

---

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/Kaede-118/Project-Snapshot.git
```

### 2. 添加到 PATH

将包含 `snapshot.bat` 的目录加入系统 PATH。

例如：

```text
D:\Tools\Project-Snapshot
```

### 3. 重新打开终端

执行：

```bash
snapshot
```

如果能够正常运行，则安装完成。

---

## 导出模式

### 默认模式

```bash
snapshot
```

特点：

* 单文件最大 5 MB
* 单文件最多导出 300 行
* 超长文件自动截断

示例：

```text
[Truncated 65 lines]
```

适用于：

* 日常项目分析
* ChatGPT 上传
* 快速代码审查

---

### FULL 模式

```bash
snapshot full
```

特点：

* 单文件最大 50 MB
* 不限制导出行数
* 不进行内容截断

适用于：

* 完整项目归档
* 深度代码审查
* 长文件分析

---

## 大文件处理

默认模式：

* 超过 5 MB 的文件将被跳过

示例：

```text
[Large file skipped: 12.4 MB]
```

FULL 模式：

* 阈值提升至 50 MB

---

## 自动过滤内容

### 目录

```text
.git
.idea
.vscode
target
build
dist
node_modules
__pycache__
.gradle
.cache
tmp
logs
```

### 编译产物

```text
.class
.jar
.war
.exe
.dll
.pyc
```

### 常见媒体文件

```text
.png
.jpg
.jpeg
.gif
.webp

.mp4
.mkv
.avi
.mov

.mp3
.wav
.flac
```

---

## 使用方法

当前目录：

```bash
snapshot
```

指定目录：

```bash
snapshot D:\Project
```

完整导出：

```bash
snapshot full
```

指定目录并完整导出：

```bash
snapshot D:\Project full
```

---

## 输出文件

默认生成：

```text
_ProjectSnapshot.txt
```

文件包含：

* 项目目录树
* 文件列表
* 源码内容
* 截断提示
* 大文件跳过提示

---

## 输出示例

```text
PROJECT TREE
================================================================================

project/
├─ src/
├─ pom.xml
└─ README.md

FILES
================================================================================

--------------------------------------------------------------------------------
src/main/java/App.java
--------------------------------------------------------------------------------

public class App {
    ...
}
```

---

## 为什么要写这个？

最初只是为了更方便地把项目提交给 ChatGPT 分析。

尝试过一些现有工具，但对于个人使用来说功能过重，因此最终重写了一个只保留核心功能的版本。

核心目标始终没有变：

> 用最少的步骤，把项目转换成 AI 能直接阅读的快照文件。

---

# English

## Introduction

Project-Snapshot is a lightweight project snapshot generator.

It scans a project directory, generates a directory tree, collects source files, and exports everything into a single text file.

Designed for:

* ChatGPT
* Claude
* Gemini
* DeepSeek
* Other LLMs

The goal is simple:

> Turn a project into a single AI-friendly snapshot file with as little friction as possible.

---

## Features

* Project tree generation
* Source code collection
* Automatic filtering of binary files
* Automatic filtering of common build directories
* Large file skipping
* Long file truncation
* FULL export mode
* Single-file output for AI analysis

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kaede-118/Project-Snapshot.git
```

### 2. Add the directory containing `snapshot.bat` to PATH

Example:

```text
D:\Tools\Project-Snapshot
```

### 3. Open a new terminal

Run:

```bash
snapshot
```

If it works correctly, installation is complete.

---

## Export Modes

### Default Mode

```bash
snapshot
```

Features:

* Maximum file size: 5 MB
* Maximum lines per file: 300
* Long files are automatically truncated

Example:

```text
[Truncated 65 lines]
```

Suitable for:

* Daily project analysis
* ChatGPT uploads
* Quick code reviews

---

### FULL Mode

```bash
snapshot full
```

Features:

* Maximum file size: 50 MB
* No line limit
* No truncation

Suitable for:

* Full project archives
* Deep code reviews
* Long source file analysis

---

## Large File Handling

Default mode:

* Files larger than 5 MB are skipped

Example:

```text
[Large file skipped: 12.4 MB]
```

FULL mode:

* Threshold increased to 50 MB

---

## Automatically Ignored Content

### Directories

```text
.git
.idea
.vscode
target
build
dist
node_modules
__pycache__
.gradle
.cache
tmp
logs
```

### Build Artifacts

```text
.class
.jar
.war
.exe
.dll
.pyc
```

### Media Files

```text
.png
.jpg
.jpeg
.gif
.webp

.mp4
.mkv
.avi
.mov

.mp3
.wav
.flac
```

---

## Usage

Current directory:

```bash
snapshot
```

Specific directory:

```bash
snapshot D:\Project
```

Full export:

```bash
snapshot full
```

Specific directory with full export:

```bash
snapshot D:\Project full
```

---

## Output File

Generated file:

```text
_ProjectSnapshot.txt
```

The snapshot includes:

* Project tree
* File list
* Source code
* Truncation notices
* Large-file skip notices

---

## Output Example

```text
PROJECT TREE
================================================================================

project/
├─ src/
├─ pom.xml
└─ README.md

FILES
================================================================================

--------------------------------------------------------------------------------
src/main/java/App.java
--------------------------------------------------------------------------------

public class App {
    ...
}
```

---

## Why?

This project started as a simple way to export projects for ChatGPT analysis.

After trying several existing tools, I found them unnecessarily complex for personal use, so I rewrote a minimal version focused on the core functionality.

The goal never changed:

> Convert a project into an AI-readable snapshot file with as little friction as possible.
