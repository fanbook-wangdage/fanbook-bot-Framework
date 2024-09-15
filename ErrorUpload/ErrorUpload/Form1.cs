using System.Runtime.InteropServices;
using Newtonsoft.Json.Linq;

namespace ErrorUpload
{
    public partial class Form1 : Form
    {
        private string data1 = "";
        private string nickname = "";
        private string shortId = "";
        private string uid = "";
        public Form1()
        {
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;
            InitializeComponent();
            try
            {
                string userFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
                string jsonFilePath = Path.Combine(userFolder, "iDreamSky", "Fanbook", "shared_preferences.json");

                var jsonData = File.ReadAllText(jsonFilePath);
                var data = JObject.Parse(jsonData);

                var userInfoJson = data["flutter.UserInfo_2"].ToString();
                var userInfo = JObject.Parse(userInfoJson);

                nickname = userInfo["nickname"].ToString();
                shortId = userInfo["username"].ToString();
                uid = userInfo["user_id"].ToString();
            }
            catch (Exception)
            {

            }

            data1 = Hwinfo(System.AppDomain.CurrentDomain.BaseDirectory + "\\hwinfo.ini", System.AppDomain.CurrentDomain.BaseDirectory);
            data1 = data1 + " \n�û�����" + nickname + " \n�û���id��" + shortId + " \nid��" + uid;
        }
        [DllImport("Ӳ���������.dll")]
        public static extern string Hwinfo(string �����ļ�·��, string ����Ŀ¼);
        private async void button2_Click(object sender, EventArgs e)
        {
            button2.Enabled = false;
            button2.Text = "�ύ��";
            string filePath = "error.log";
            string content = "��ȡʧ��";
            try
            {
                content = File.ReadAllText(filePath);
            }
            catch (Exception)
            {

            }

            string url = "http://124.221.67.43/webapi/bot/sendBug?text="+data1+"\n\n�û�������\n"+textBox1.Text+"\n\n������Ϣ��"+content;
            string response = await SendGetRequestAsync(url);
            button2.Text = "���ύ";
            button1.Text = "���";
        }


        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        private async Task<string> SendGetRequestAsync(string url)
        {
            using (HttpClient client = new HttpClient())
            {
                try
                {
                    HttpResponseMessage response = await client.GetAsync(url);
                    response.EnsureSuccessStatusCode();
                    string responseBody = await response.Content.ReadAsStringAsync();
                    return responseBody;
                }
                catch (HttpRequestException ex)
                {
                    return $"�������: {ex.Message}";
                }
            }
        }
    }
}
