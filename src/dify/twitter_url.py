def main(origin_url) -> dict:
    twitter_urls = []
    
    # 遍历输入数据
    for item in origin_url:
        # 检查是否有valueRange字段
        if 'valueRange' in item and 'values' in item['valueRange']:
            values = item['valueRange']['values']
            
            # 跳过第一行（标题行）
            for row in values[1:]:
                if row and len(row) > 0:
                    # 获取第一个元素（包含URL信息的数组）
                    url_data = row[0]
                    
                    # 如果url_data是数组，取第一个元素
                    if isinstance(url_data, list) and len(url_data) > 0:
                        url_obj = url_data[0]
                        
                        # 检查是否有link字段
                        if 'link' in url_obj:
                            link = url_obj['link']
                            
                            # 将x.com转换为twitter.com
                            if 'x.com' in link:
                                link = link.replace('x.com', 'twitter.com')
                            
                            twitter_urls.append(link)
    
    return {
        "twitter_url": twitter_urls
    }