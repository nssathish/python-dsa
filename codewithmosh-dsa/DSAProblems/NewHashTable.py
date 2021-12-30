class Entry:
    def __init__(self, K, V) -> None:
        self.K = K
        self.V = V
        self.next = None


class HashTable:
    def __init__(self, table_size=100) -> None:
        self.table_size = table_size
        self.table = [ None ] * table_size
    
    def put(self, K: int, V: str) -> None:
        new_entry = Entry(K, V)
        idx = self._hash_code_for(K)
        self._insert_into(idx, new_entry)
    
    def get(self, K) -> str:
        idx = self._hash_code_for(K)
        return self._fetch(idx, K)

    def remove(self, K) -> str:
        idx = self._hash_code_for(K)
        return self._fetch_and_delete(idx, K)

    def _hash_code_for(self, K: int) -> int:
        return K % self.table_size

    def _insert_into(self, idx, new_entry) -> None:
        if self.table[idx] is None:
            self.table[idx] = new_entry
        else:
            existing_entries = self.table[idx]
            while existing_entries.next is not None:
                existing_entries = existing_entries.next
            existing_entries.next = new_entry
    
    def _fetch(self, idx, K):
        if self.table[idx] is None:
            return None
        
        entries = self.table[idx]
        return self._search_value_for(K, entries)
    
    def _search_value_for(self, K, entries) -> str:
        while entries is not None and entries.K != K:
            entries = entries.next
        
        return None if entries is None else entries.V

    def _fetch_and_delete(self, idx, K) -> str:
        entries = self.table[idx]
        while entries is not None and \
            entries.next is not None and \
                entries.next.K != K and \
                    entries.K != K:
                    entries = entries.next
        
        if entries is None:
            return ""
        
        if entries.K == K:
            self.table[idx] = entries.next
            return entries.V
        
        if entries.next.K == K:
            delete_entry = entries.next
            entries.next = None
            return delete_entry


    
if __name__ == '__main__':
    new_hash_table = HashTable()
    new_hash_table.put(1, 'sathish')
    new_hash_table.put(11, 'seethu')
    print(new_hash_table.get(11))
    print(new_hash_table.remove(11))
    print(new_hash_table.get(11))
    print(new_hash_table.get(1))