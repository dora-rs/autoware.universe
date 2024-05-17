from typing import Callable, Optional
from dora import DoraStatus
import json
from json import *
import dora
import pyarrow as pa
import numpy as np
from typing import Dict, List
import time
import pickle

class Operator:
    def __init__(self) -> None:
        self.pose = {
            'header': 
            {
                'frame_id': "map",
                'stamp': 
                {
                    'sec': 0,
                    'nanosec': 0,
                }
            },
            "orientation": 
            {
                "w": 0.0, 
                "x": 0.0, 
                "y": 0.0, 
                "z": 0.0,
            },
            "position": 
            {
                "x": 0.0, 
                "y": 0.0, 
                "z": 0.0,
                "vx": 0.0, 
                "vy": 0.0, 
                "vz": 0.0,
            }
        }
    def on_event(
        self,
        dora_event,
        send_output,
    ) -> DoraStatus:
        if dora_event["type"] == "INPUT":
            return self.on_input(dora_event, send_output)
        return DoraStatus.CONTINUE
    
    def on_input(
        self,
        dora_input: dict,
        send_output: Callable[[str, bytes], None],
    ):
        if "DoraNavSatFix" == dora_input["id"]:
            print("DoraNavSatFix")
            data = dora_input["value"].to_pylist()
            json_string = ''.join(chr(int(num)) for num in data)
            # js
            print(json_string)
            # 假设 json_string 是收到的 JSON 数据字符串
            json_dict = json.loads(json_string)
            # 从 JSON 数据中提取关键字
            self.pose["header"]["frame_id"] = "gnss"
            # pose["header"]["stamp"]["sec"] = jsson_dict["sec"]
            # pose["header"]["stamp"]["nanosec"] = json_dict["nanosec"]
            self.pose["position"]["x"] = json_dict["x"]
            self.pose["position"]["y"] = json_dict["y"]
            self.pose["position"]["z"] = json_dict["z"]
            self.pose["position"]["vx"] = 0.0
            self.pose["position"]["vy"] = 0.0
            self.pose["position"]["vz"] = 0.0

        if "DoraQuaternionStamped" == dora_input["id"]:
            print("DoraQuaternionStamped")
            data = dora_input["value"].to_pylist()
            json_string = ''.join(chr(int(num)) for num in data)
            # jss
            print(json_string)
            # 假设 json_string 是收到的 JSON 数据字符串
            json_dict = json.loads(json_string)
            self.pose["header"]["frame_id"] = "gnss"
            self.pose["header"]["stamp"]["sec"] = json_dict["sec"]
            self.pose["header"]["stamp"]["nanosec"] = json_dict["nanosec"]
            self.pose["orientation"]["x"] = json_dict["x"]
            self.pose["orientation"]["y"] = json_dict["y"]
            self.pose["orientation"]["z"] = json_dict["z"]
            self.pose["orientation"]["w"] = json_dict["w"]
  
        # 发布JSON-DoraNavSatFix消息
        json_string = json.dumps(self.pose, indent=4)  # 使用indent参数设置缩进宽度为4
        print("pose")
        print(json_string)
        json_bytes = json_string.encode('utf-8')
        send_output("DoraGnssPose",json_bytes,dora_input["metadata"],)


        return DoraStatus.CONTINUE


    
