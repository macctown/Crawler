import  os

def create_project_dir(directory):
    if  not os.path.exists(directory):
        print('creating project ' + directory)
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_data_to_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_data_to_file(crawled, '')


def write_data_to_file(file_name, data):
    f = open(file_name, 'w')
    f.write(data)
    f.close()


def write_set_to_file(file_name, dataset):
    with open(file_name, 'w') as file:
        for data in dataset:
            file.write(data + '\n')


def append_to_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(file_name):
    with open(file_name, 'w'):
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'r') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(file_name, links):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")


