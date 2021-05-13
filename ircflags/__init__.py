from typing  import List, Set
from os.path import isfile
import json

class Flags(object):
        def __init__(self,
                file: str,
                validflags: str):

            if not validflags.isalpha():
                raise ValueError("Flags can only be letters of the alphabet")

            self.file        = file
            self.validflags  = sorted(validflags)
            self.database    = {}

            self._from_file()

        def _serialize(self, value: Set[str]) -> List[str]:
            return list(value)

        def _deserialize(self, value: List[str]) -> Set[str]:
            return set(value)

        def _from_file(self):
            if isfile(self.file):
                with open(self.file) as db_file:
                    database = json.loads(db_file.read())

                for t in database.keys():
                    if not t in self.database.keys():
                        self.database[t] = {}
                    self.database[t].update({
                        k: self._deserialize(v) for k,v in database[t].items()
                    })

        def _write(self):
            database_serialized = {
                t: {
                    k: self._serialize(v) for k,v in self.database[t].items()
                } for t in self.database.keys()
            }
            data = json.dumps(database_serialized, indent=4, sort_keys=True)
            with open(self.file, "w") as db_file:
                db_file.write(data)

        def getFlags(self,
                user: str,
                default: str = '',
                channel: str = None):

            user = user.lower()

            if channel and channel.lower() in self.database.keys() and user in self.database[channel]:
                target = channel.lower()
            else:
                target = "global"

            try:
                value = self.database[target][user]
            except KeyError:
                value = default

            return "".join(sorted(value))

        def setFlags(self,
                user: str,
                value: str,
                channel: str = None):

            user = user.lower()

            if channel:
                target = channel.lower()
            else:
                target = "global"

            if not target in self.database.keys():
                self.database[target] = {}

            flags = {f for f in self.database[target].get(user, "")}
            op = value[0]
            if not op in "+-":
                raise ValueError(f"{op} is not a valid operator")
            for c in value[1:]:
                if c in "+-":
                    op = c
                elif c in self.validflags:
                    if op == "+" and not c in flags:
                        flags.add(c)
                    elif op == "-" and c in flags:
                        flags.remove(c)
                elif c == "*":
                    if op == "+":
                        flags = set("".join(self.validflags))
                    elif op == "-":
                        flags = set()
                else:
                    raise ValueError(f"{c} is not a valid flag")

            self.database[target][user] = flags
            self._write()
