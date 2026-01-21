import json
from neo4j import GraphDatabase
from configuration.config import *

# 读取文件
def read_json_file(path):
    # 读取json文件中的数据
    with open(path, "r", encoding="utf-8") as f:
        datas = [ json.loads(line) for line in f ]
        return datas

# 写入neo4j工具类
class Neo4jWriter:
    def __init__(self):
        self.driver = GraphDatabase.driver(**NEO4J_CONFIG)
    # 写入节点批量,固定标签
    def write_nodes(self, label:str, properties:list[dict]):
        data_key = properties[0].keys()
        property_state = ",".join([ f"{key}:item.{key}" for key in data_key ])
        cypher = f"""
            UNWIND $batch AS item
            MERGE (:{label} { {property_state} }) 
        """
        self.driver.execute_query(cypher,batch=properties)

    # 写入关系
    def write_relations(self, type:str, start_label:str, end_label:str, relations:list[dict]):
        cypher = f"""
            UNWIND $batch AS item
            MATCH (start:{start_label} {{id:item.start_id}}), (end:{end_label} {{id:item.end_id}}) 
            MERGE (start)-[:{type}]->(end)
        """
        self.driver.execute_query(cypher,batch=relations)


if __name__ == "__main__":
    datas = read_json_file(DATA_DIR/"knowledge_graph"/"medical_kg.jsonl")
    print(datas[0])


