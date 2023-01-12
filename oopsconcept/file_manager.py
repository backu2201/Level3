from  ADprinciple import FileSearcher
class SearchManager:
    def __init__(self):
        pass
    def search(self,file_name,drives):
        print("this is a search engine")
        searcher_threads = []
        file_searchers = []
        for drive in drives:
            print(drives)
            file_searcher = FileSearcher()
            file_searcher.search_for_file(drive, file_name)
            search_thread = Thread()
            search_thread.start(file_searcher)
            file_searchers.append(file_searcher)
            searcher_threads.append(search_thread)
        for searcher_thread in searcher_threads:
            searcher_thread.join()
        search_results = []
        for file_searcher in file_searchers:
            search_results.append(file_searcher, file_name)
        return search_results
if __name__=='__main__':
    obj=SearchManager()
    print(obj.search(("MT1.txt")))
