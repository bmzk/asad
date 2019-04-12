'''读写Json文件'''
import json
obj={"a":'a',"b":2}


def dump_():
    file_w=open('f.json','w',encoding='utf-8')
    json_str=json.dumps(obj)
    print('dump_s',json_str)
    json.dump(json_str,file_w)
    file_w.close()

def dump_s():
    file_w=open('f.json','w',encoding='utf-8')
    json_str=json.dumps(obj)
    print('dump_s',json_str)
    json.dump(json_str,file_w)
    file_w.close()


file_r=open('f.json','r')
json_str=json.load(file_r)
json.loads(json_str)
file_r.close()


print('b',9)
print('b',9)
