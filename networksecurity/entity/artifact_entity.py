from dataclasses import dataclass

@dataclass
class DataIngestionArfifact:
    trained_file_path:str
    test_file_path:str