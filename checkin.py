import os
import json
import yaml

if __name__ == '__main__':
    if os.getenv('GITHUB_ACTIONS') == 'true':
        profiles = json.loads(os.getenv('profiles'))
    else:
        with open('config/profiles.json', 'r', encoding='utf-8') as f:
            profiles = json.load(f)

    with open('config/config.yaml.example', 'r', encoding='utf-8') as f:
        config_example = yaml.load(f, Loader=yaml.FullLoader)

    # 生成配置文件
    for profile in profiles:
        config = config_example.copy()
        config['account']['cookie'] = profile['cookie']
        config['account']['stoken'] = profile['stoken']
        with open(f'config/{profile["name"]}.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True)

    try:
        # 运行主脚本
        os.system('python main_multi.py autorun')
    finally:
        # 删除配置文件
        for profile in profiles:
            os.remove(f'config/{profile["name"]}.yaml')