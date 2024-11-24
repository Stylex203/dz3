import re
import yaml
import sys

class ConfigParser:
    def __init__(self):
        self.constants = {}

    def parse(self, lines):
        output = {}
        for line_no, line in enumerate(lines, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                if line.startswith("def"):
                    self._parse_definition(line)
                elif line.startswith("@{"):
                    value = self._evaluate_constant(line)
                    print(f"Evaluated: {value}")
                else:
                    key, value = self._parse_key_value(line)
                    output[key] = value
            except ValueError as e:
                raise SyntaxError(f"Error on line {line_no}: {e}")
        return output

    def _parse_definition(self, line):
        match = re.match(r"def\s+([a-zA-Z]+)\s*:=\s*(.+)", line)
        if not match:
            raise ValueError(f"Invalid constant definition: {line}")
        name, value = match.groups()
        self.constants[name] = self._parse_value(value)

    def _evaluate_constant(self, line):
        match = re.match(r"@\{([a-zA-Z]+)\}", line)
        if not match:
            raise ValueError(f"Invalid constant reference: {line}")
        name = match.group(1)
        if name not in self.constants:
            raise ValueError(f"Undefined constant: {name}")
        return self.constants[name]

    def _parse_key_value(self, line):
        match = re.match(r"([a-zA-Z]+)\s*:\s*(.+)", line)
        if not match:
            raise ValueError(f"Invalid key-value pair: {line}")
        key, value = match.groups()
        if value.startswith("@{") and value.endswith("}"):
            value = self._evaluate_constant(value)
            return key, value
        return key, self._parse_value(value)

    def _parse_value(self, value):
        if isinstance(value, int) or isinstance(value, list):
            return value
        value = value.strip()
        if value.isdigit():
            return int(value)
        elif value.startswith("#(") and value.endswith(")"):
            return self._parse_array(value)
        elif re.match(r"[a-zA-Z]+", value):
            return value
        else:
            raise ValueError(f"Invalid value: {value}")

    def _parse_array(self, value):
        content = value[2:-1].strip()
        return [self._parse_value(v) for v in content.split()]

def main():
    input_file = "input.txt"
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

        config_parser = ConfigParser()
        parsed_data = config_parser.parse(lines)
        yaml.dump(parsed_data, sys.stdout, allow_unicode=True)

    except FileNotFoundError:
        print(f"Error: File {input_file} not found", file=sys.stderr)
        sys.exit(1)
    except SyntaxError as e:
        print(f"Syntax Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
