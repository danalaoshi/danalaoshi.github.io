---
layout: default
title: 编程教程中心
description: 全面的编程学习资源库
nav_order: 1
---

# 欢迎来到编程教程中心

这里汇集了多门编程语言和技术的学习资源，从基础到高级，帮助您系统学习编程。

## 📚 可用课程

<div class="courses-grid">
  {% for book in site.books %}
    <div class="course-card">
      <div class="course-icon">📚</div>
      <h3>{{ book.name }}</h3>
      <p>系统学习 {{ book.name }} 的完整知识体系</p>
      <a href="{{ '/' | append: book.dir | append: '/' | relative_url }}" class="course-button">
        开始学习
      </a>
    </div>
  {% endfor %}
</div>

## 🎯 学习特色

- **系统化教程** - 每门课程都有完整的知识体系
- **实践导向** - 丰富的代码示例和练习
- **持续更新** - 内容会根据技术发展持续更新

## 💡 使用建议

1. 按顺序学习各章节内容
2. 动手实践每个代码示例
3. 完成章节后的练习题目
4. 结合实际项目应用所学知识