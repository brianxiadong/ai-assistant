import yaml

class TranslatorConfig:
    _instance = None  # 初始化一个类变量，用于存储单例实例

    def __new__(cls):  # 重写__new__方法以实现单例
        if not cls._instance:  # 如果当前类的实例不存在
            cls._instance = super(TranslatorConfig, cls).__new__(cls)  # 创建新实例并赋值给类变量
        return cls._instance  # 返回已存在的实例

    def initialize(self, args):  # 初始化方法，从命令行参数或默认配置文件加载配置
        file_path = args.config_file if args.config_file is None else "config/config.yaml"  # 设置配置文件路径
        with open(file_path, 'r') as file:  # 打开配置文件
            data = yaml.safe_load(file)  # 安全地加载yaml配置数据

        # 更新配置数据，使用命令行参数覆盖配置文件中的值
        for attr, value in vars(args).items():  # 遍历命令行参数
            if attr is not None and value is not None:  # 如果参数非空
                data[attr] = value  # 更新配置数据

        self._config_data = data  # 将更新后的配置数据保存在实例变量中
        return data  # 返回配置数据

    def __getattr__(self, name):  # 当尝试访问未定义的属性时，从配置数据中查找
        # Try to get attribute from _config
        if name in self._config_data:  # 如果属性存在于配置数据中
            return self._config_data[name]  # 返回该属性的值
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")  # 抛出AttributeError异常，提示属性不存在
