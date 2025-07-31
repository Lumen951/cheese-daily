import json
from src.dify.paper_output import main

# 测试数据
test_explained_paper = [
    "第一篇论文的详细分析内容",
    "第二篇论文的详细分析内容", 
    "第三篇论文的详细分析内容",
    "第四篇论文的详细分析内容",
    "第五篇论文的详细分析内容"
]

test_classified_category = [
    "应用体系",
    "应用体系", 
    "认知模型",
    "认知模型",
    "多模态"
]

test_paper_url = [
    "https://arxiv.org/abs/paper1",
    "https://arxiv.org/abs/paper2",
    "https://arxiv.org/abs/paper3",
    "https://arxiv.org/abs/paper4",
    "https://arxiv.org/abs/paper5"
]

test_cheese_summary = "这是一个综合性的研究总结，涵盖了多个领域的最新进展。"

# 测试合并功能
result = main(test_explained_paper, test_classified_category, test_paper_url, test_cheese_summary)

# 打印结果
print("合并结果 (包含cheese_summary):")
print(json.dumps(result, ensure_ascii=False, indent=2))

# 验证结果
print(f"\n验证:")
print(f"输入explained_paper长度: {len(test_explained_paper)}")
print(f"输入classified_category长度: {len(test_classified_category)}")
print(f"输入paper_url长度: {len(test_paper_url)}")
print(f"输出合并结果长度: {len(result['paper_output'])}")

# 检查每个合并项（现在是字符串格式）
for i, item in enumerate(result['paper_output']):
    if i < len(result['paper_output']) - 1:  # 不是最后一个元素
        print(f"\n第{i+1}项合并 (字符串格式):")
        print(f"  内容: {item}")
        
        # 解析字符串验证内容
        parsed_item = json.loads(item)
        print(f"  解析后的explained_content: {parsed_item['explained_content'][:50]}...")
        print(f"  解析后的classified_category: {parsed_item['classified_category']}")
        print(f"  解析后的paper_url: {parsed_item['paper_url']}")
    else:  # 最后一个元素是cheese_summary
        print(f"\n最后一项 (cheese_summary):")
        print(f"  内容: {item}") 