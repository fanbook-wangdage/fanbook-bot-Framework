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
        private string url; // �洢��JSON��ȡ��URL

        public Form1()
        {
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;
            InitializeComponent();
            LoadDataAsync(); // �첽��������
        }

        // ���������ڷ����л�JSON����
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
                        url = data.url; // ��URL�����Թ�����ʹ��
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("�޷���ȡ����: " + ex.Message);
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
                        FileName = url, // ʹ�ô�JSON��ȡ��url
                        UseShellExecute = true
                    };
                    Process.Start(psi);

                    // �رմ���
                    this.Close();
                }
                else
                {
                    MessageBox.Show("URLΪ�գ��޷�����ҳ��");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("�޷�����ҳ: " + ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // �رմ���
            this.Close();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
