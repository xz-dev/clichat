import multiprocessing as mp

#  import Ui
#  import handlePostData
#  import startMojoWeb
from post.PostServer import PostServer
from data import *

if __name__ == '__main__':
    try:
        mojo_webqq_config_path = 'webqq.pl'
        manager = mp.Manager()
        POST_data = manager.list()
        all_message_dict = manager.dict()
        Data = data.Data()
        PostServer = PostServer()
        HandlePostData = data_handle.HandlePostData()
        # POST服务器
        post_server = mp.Process(
            target=PostServer.run, args=(Data.post_data.data, ))
        post_handle = mp.Process(
            target=HandlePostData.run, args=(Data, ))
        post_server.start()
        post_handle.start()
        post_handle.join()
        post_server.join()
        #  # mojo-webqq服务器
        #  webqq_server = mp.Process(
        #      target=startMojoWeb.startMojoWebQQ,
        #      args=(mojo_webqq_config_path,))
        #  # POST信息处理
        #  handle_friend_message = mp.Process(
        #      target=handlePostData.getMessage,
        #      args=(POST_data, all_message_dict))
        #  # 显示主UI
        #  ui = mp.Process(
        #      target=Ui.main, args=(all_message_dict, POST_data, ))
        #  startMojoWeb.stopMojoWebQQ()  # 完全关闭MojoWebQQ
        #  post_server.start()           # 启动POST服务器
        #  webqq_server.start()          # 启动MojoWebQQ
        #  # 扫码后启动好友消息处理程序
        #  #  handle_friend_message.start()
        #  # 启动主页UI
        #  ui.start()
        #  ui.join()
        #  # UI关闭, POST_data = False 以示程序关闭
        #  POST_data = False
        #  handle_friend_message.join()
        #  webqq_server.join()
        #  post_server.join()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
