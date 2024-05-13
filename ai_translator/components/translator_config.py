import yaml


class TranslatorConfig:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(TranslatorConfig, cls).__new__(cls)
        return cls._instance

    def initialize(self, args):

        file_path = args.config_file if args.config_file is None else "config/config.yaml"

        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        #覆盖字典中的数据
        for attr, value in vars(args).items():
            if attr is not None and value is not None:
                data[attr] = value

        self._config_data = data

        return data

    def __getattr__(self, name):
        # Try to get attribute from _config
        if name in self._config_data:
            return self._config_data[name]
        raise AttributeError(f"'TranslationConfig' object has no attribute '{name}'")
