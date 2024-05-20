# 1. 接收GNSS

使用指令：

```bash
cd ~/autoware.universe/localization/ekf_localizer
dora up
dora start dataflow.yml --name test
```

接收GNSS消息格式

```json
{
    "header": {
        "frame_id": "gnss",
        "stamp": {
            "sec": 0,
            "nanosec": 1
        }
    },
    "orientation": {
        "w": 5,
        "x": 2,
        "y": 3,
        "z": 4
    },
    "position": {
        "x": 29.74679792,
        "y": 106.55386011,
        "z": 258.89,
        "vx": 0.0,
        "vy": 0.0,
        "vz": 0.0
    }
}
```

