import os
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

# 更新为模式文件的实际路径
SCHEMA_PATH = 'C:\\Users\\kevin\\OneDrive - The University Of Hong Kong\\Desktop\\LinkML\\How_to\\KS_LinkML\\src\\ks_linkml\\schema\\ks_linkml.yaml'

def validate_schema(schema_path):
    try:
        # Load the schema
        schema_view = SchemaView(schema_path)
        # Optionally, you can print out the classes and slots to verify they are loaded correctly
        for class_name in schema_view.all_classes():
            print(f"Class: {class_name}")
            for slot in schema_view.class_induced_slots(class_name):
                print(f"  Slot: {slot.name}")
        print("Schema validation passed.")
    except Exception as e:
        print(f"Schema validation failed: {e}")

if __name__ == "__main__":
    validate_schema(SCHEMA_PATH)