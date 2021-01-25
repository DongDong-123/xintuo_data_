import os
import re
import shutil
import time

def run(aim):
    path = os.getcwd()
    aim_path = os.path.join(path, aim)
    name_list = os.listdir(aim_path)
    trade = name_list.pop(11)
    print(name_list)

    new_folder = str(int(aim)+1)
    # new_folder = '20200920'
    # full_new_path = [os.path.join(os.path.join(path,new_folder), el) for el in name_list]
    full_new_path = os.path.join(os.path.join(path,new_folder), re.sub('\d+', new_folder, trade))
    ful_old_path = os.path.join(aim_path, trade)
    # ful_old_path = [os.path.join(aim_path, el) for el in name_list]
    # for ind, pa in enumerate(ful_old_path):
    change_name(name_list,aim_path, os.path.join(path,new_folder), new_folder)

    update_data(ful_old_path, new_folder, full_new_path)


def change_name(name_list,old_path, new_path, dates):

    if not os.path.exists(os.path.join(os.getcwd(), dates)):
        os.mkdir(os.path.join(os.getcwd(), dates))

    for li in name_list:
        print("-----",li,"------------")
        shutil.copy(os.path.join(old_path,li), new_path)



    time.sleep(3)
    for elem in name_list:
        elem_new = re.sub('\d+', dates, elem)
        os.rename(os.path.join(new_path, elem), os.path.join(new_path, elem_new))


def update_data(old_file, dates, new_file):
    with open(old_file, 'r', encoding='utf-8') as f:
        result = f.readlines()
        # print(result)

    after = []
    for res in result:
        pro1 = res.split('|')
        # print(pro1[14])
        if pro1[14].isdigit():
            tt = pro1[0][0]
            t2 = str(int(pro1[0][1:])+ 100)
            pro1[0] = tt + t2
            pro1[14] = dates
            elem_new = '|'.join(pro1)
            after.append(elem_new)
        else:
            continue
    # if not os.path.exists(new_file):
    #     with open(new_file, 'r', encoding='utf-8') as f:
    #         pass
    with open(new_file, '+a',encoding='utf-8') as f:
        f.writelines(after)


if __name__ == "__main__":
    # change_name(name_list)

    # name = 'transaction_20190521.txt'
    # update_data(path2,'20190522')
    aim = '20200920'
    # aim = '20200801'
    for i in range(7):
        run(aim)
        aim = str(int(aim) + 1)
