'''读写Json文件'''
import json
import random 
d={"a":'a',"b":2,'c':0.5,'d':[1,2,'y']}

def dump_():
    file_w=open('f.json','w+',encoding='utf-8')
    obj={"a":'a',"b":2}
    for i in 'abcdefg':
        obj['a']=i
        obj['b']=random.randint(10,99)
        print('dump_',obj)
        json.dump(obj,file_w,indent=5)
    file_w.close()

def dump_s():
    json_str='0'
    file_w=open('fs.json','w+',encoding='utf-8')
    obj={"a":'a',"b":2}
    for i in 'abcdefg':
        obj['a']=i
        obj['b']=random.randint(10,99)
        json_str=json.dumps(obj)
        print('dump_s',json_str)
        json.dump(json_str,file_w)
        json.dump(json.dumps('\n'),file_w)
    file_w.close()

def load():
    file_r=open('f.json')
    input('input... 1')
    json_str=json.load(file_r)
    input('input... 2')
    print(json_str)
    file_r.close()


print('b',9)
#dump_()
for i in d:
    print(i)
print('b',9)
#load()
print('c',9)










