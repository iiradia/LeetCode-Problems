class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        items = {"Items": ["Table"], "Table" : {}}
        for order in orders:
            
            try:
                if order[2] not in items["Items"]:
                    items["Items"].append(order[2])
                item = items["Table"][order[1]]
                try:
                    item[order[2]] += 1
                except:
                    item[order[2]] = 1
            except:
                items["Table"][order[1]] = {order[2]:1}
            
        tables = []
        items["Items"].sort()
        items["Items"].remove("Table")
        items["Items"].insert(0, "Table")
        i = 0
        for key,val in items["Table"].items():
            tables.append([])
            tables[i].append(int(key))
            for food in items["Items"][1:]:
                try:
                    tables[i].append(str(val[food]))
                except:
                    tables[i].append("0")
            i+=1
        table_to_return = [items["Items"]]
        for table in sorted(tables):
            table[0] = str(table[0])
            table_to_return.append(table)
        return table_to_return
            
        