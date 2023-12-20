from batch.lib.interface.init import Init
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo


class Bootstrap:

    func_id: Optional[str] = None
    curr_time: Optional[datetime] = None
    curr_time_str: Optional[str] = None

    def __init__(self, init):
        self.func_id = init.get_func_id()
        print(self)
        # 获取当前时间
        self.current_time = datetime.now(ZoneInfo("Asia/Tokyo"))  # 使用 UTC 时区
        print("当前时间 (日本):", self.current_time)
        self.curr_time_str = self.current_time.strftime("%Y-%m-%d %H:%M:%S")
        print("当前时间:", self.curr_time_str)

        # 查询

        # 添加

        # error -> 6B



        pass
