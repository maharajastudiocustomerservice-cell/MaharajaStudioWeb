import json

with open(r'C:\Users\Soutick\.gemini\antigravity\brain\5a061939-da90-49f9-90ae-df800c809452\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        d = json.loads(line)
        if d.get('type') == 'USER_INPUT':
            print(f"Step {d.get('step_index')}: content={repr(d.get('content'))}, media_count={len(d.get('media', []))}")
            if d.get('media'):
                for m in d.get('media'):
                    print("   media:", m.get('uri'))
