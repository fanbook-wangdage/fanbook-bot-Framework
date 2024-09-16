using System;
using System.Diagnostics;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;

namespace WinFormsApp3
{
    public partial class Form1 : Form
    {
        private string url; // 存储从JSON获取的URL

        public Form1()
        {
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;
            InitializeComponent();
            LoadDataAsync(); // 异步加载数据
        }

        // 定义类用于反序列化JSON数据
        public class Data
        {
            public string t1 { get; set; }
            public string t2 { get; set; }
            public string url { get; set; }
        }

        private async Task LoadDataAsync()
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    string json = await client.GetStringAsync("https://124.221.67.43/hj_data.json");
                    Data data = JsonConvert.DeserializeObject<Data>(json);

                    if (data != null)
                    {
                        label1.Text = data.t1;
                        label3.Text = data.t2;
                        url = data.url; // 将URL保存以供后续使用
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("无法获取数据: " + ex.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                if (!string.IsNullOrEmpty(url))
                {
                    ProcessStartInfo psi = new ProcessStartInfo
                    {
                        FileName = url, // 使用从JSON获取的url
                        UseShellExecute = true
                    };
                    Process.Start(psi);

                    // 关闭窗口
                    this.Close();
                }
                else
                {
                    MessageBox.Show("URL为空，无法打开网页。");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("无法打开网页: " + ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 关闭窗口
            this.Close();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
