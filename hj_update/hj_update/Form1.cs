using System;
using System.IO;
using System.IO.Compression;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace hj_update
{
    public partial class Form1 : Form
    {
        private string downloadUrl;
        private string t1;
        private long totalFileSize;
        public static float t;

        public Form1()
        {
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;
            InitializeComponent();
            InitializeData();
        }

        private async void InitializeData()
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    var response = await client.GetStringAsync("https://124.221.67.43/hj_data.json");
                    dynamic jsonData = Newtonsoft.Json.JsonConvert.DeserializeObject(response);

                    label3.Text = jsonData.v.ToString();
                    label8.Text = jsonData.info.ToString();
                    downloadUrl = jsonData.mainurl.ToString();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error fetching data: " + ex.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(downloadUrl))
            {
                progressBar1.Visible = true;
                button1.Enabled = false;
                button2.Enabled = false;
                DownloadFile(downloadUrl);
            }
            else
            {
                MessageBox.Show("Download URL is not available.");
            }
        }

        private async void DownloadFile(string url)
        {
            using (WebClient client = new WebClient())
            {
                client.DownloadProgressChanged += new DownloadProgressChangedEventHandler(DownloadProgressCallback);
                client.DownloadFileCompleted += new System.ComponentModel.AsyncCompletedEventHandler(DownloadFileCompletedCallback);

                try
                {
                    Uri uri = new Uri(url);
                    string fileName = Path.GetFileName(uri.LocalPath);
                    string destinationPath = Path.Combine(Directory.GetCurrentDirectory(), fileName);

                    // Get file size
                    HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uri);
                    request.Method = "HEAD";
                    using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
                    {
                        totalFileSize = response.ContentLength;
                        t = totalFileSize / 1024;
                        t = t / 1024;
                        t1 = t.ToString("0.00");

                        //label9.Text = "File Size: " + t + " bytes";
                    }

                    await client.DownloadFileTaskAsync(uri, destinationPath);

                    // Unzip file after download
                    label9.Text = "解压中";
                    string extractPath = Directory.GetCurrentDirectory();
                    ZipFile.ExtractToDirectory(destinationPath, extractPath, true);
                    label9.Text = "已完成";
                    button2.Enabled = true;
                    button2.Text = "完成";
                    button1.Text = "已安装";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error downloading file: " + ex.Message);
                }
            }
        }

        private void DownloadProgressCallback(object sender, DownloadProgressChangedEventArgs e)
        {
            progressBar1.Value = e.ProgressPercentage;
            float b;
            b = e.BytesReceived;
            b = b / 1024;
            b = b / 1024;
            string show = b.ToString("0.00");
            label9.Text = $"下载中，已经下载 {show}MB 总大小： {t1}MB";
        }

        private void DownloadFileCompletedCallback(object sender, System.ComponentModel.AsyncCompletedEventArgs e)
        {
            if (e.Error != null)
            {
                MessageBox.Show("Error: " + e.Error.Message);
            }
            else if (e.Cancelled)
            {
                MessageBox.Show("Download cancelled.");
            }
            else
            {
                label9.Text = "下载完成";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
