class Solution:
    def interpret(self, command: str) -> str:
        goal={"G":"G", "()":"o", "(al)":"al"}
        out=""
        for i in range(len(command)):
            if command[i]=="G":
                out+="G"
            elif command[i]=="(":
                if command[i+1]==")":
                    out+="o"
                else:
                    out+="al"
        return out
        