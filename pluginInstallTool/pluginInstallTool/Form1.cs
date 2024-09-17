using Newtonsoft.Json;
using System.IO;
using System.Net.Http;

namespace pluginInstallTool
{
    public partial class Form1 : Form
    {
        private PluginList pluginList; // Store the plugin list globally
        private string pluginJsonPath = "plugin.json"; // Path to local plugin.json file
        private string pluginFolderPath = "plugin"; // Folder to save downloaded files

        public Form1()
        {
            InitializeComponent();
            this.Load += Form1_Load;
            listBox1.SelectedIndex = -1;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;

            // Ensure the plugin folder exists
            if (!Directory.Exists(pluginFolderPath))
            {
                Directory.CreateDirectory(pluginFolderPath);
            }
        }

        private async Task<string> GetJsonFromUrlAsync(string url)
        {
            using (HttpClient client = new HttpClient())
            {
                return await client.GetStringAsync(url);
            }
        }

        private async void Form1_Load(object sender, EventArgs e)
        {
            string url = "http://124.221.67.43/plugin_v2.json";
            string json = await GetJsonFromUrlAsync(url);
            pluginList = JsonConvert.DeserializeObject<PluginList>(json);

            foreach (var plugin in pluginList.List)
            {
                listBox1.Items.Add(plugin.Name);
            }

            listBox1.SelectedIndexChanged += (s, ev) =>
            {
                if (listBox1.SelectedIndex != -1)
                {
                    var selectedPlugin = pluginList.List[listBox1.SelectedIndex];
                    label3.Text = selectedPlugin.Name;
                    label4.Text = selectedPlugin.Info;
                    label11.Text = selectedPlugin.Version;
                    label9.Text = selectedPlugin.Date;
                    label6.Text = selectedPlugin.Author.Name;
                    label7.Text = selectedPlugin.Author.Labels;
                    label13.Text = selectedPlugin.File.Type;
                    pictureBox1.Load(selectedPlugin.Author.Img);
                }
            };
        }

        private async void button2_Click(object sender, EventArgs e)
        {
            button2.Text = "正在安装";
            button2.Enabled = false;
            button1.Enabled = false;
            if (listBox1.SelectedIndex == -1)
            {
                MessageBox.Show("请选择一个插件！");
                button2.Text = "安装";
                button1.Enabled = true;
                button2.Enabled = true;
                return;
            }

            var selectedPlugin = pluginList.List[listBox1.SelectedIndex];

            // Step 1: Load existing plugin.json
            PluginList localPluginList = LoadLocalPluginList();

            // Step 2: Check if the selected plugin is already in the local list
            if (localPluginList.List.Any(p => p.Name == selectedPlugin.Name))
            {
                MessageBox.Show("插件已存在于本地列表中！");
                button2.Text = "安装";
                button1.Enabled = true;
                button2.Enabled = true;
                return;
            }

            // Step 3: Add selected plugin to the local plugin.json list
            localPluginList.List.Add(new Plugin
            {
                Name = selectedPlugin.Name,
                Info = selectedPlugin.Info,
                Version = selectedPlugin.Version,
                Date = selectedPlugin.Date,
                Author = selectedPlugin.Author,
                File = selectedPlugin.File
            });

            // Step 4: Save updated list back to plugin.json
            SaveLocalPluginList(localPluginList);
            // 获取url中的文件名
            string fileName = Path.GetFileName(selectedPlugin.File.Url);
            // Step 5: Download the plugin file
            await DownloadFileAsync(selectedPlugin.File.Url, Path.Combine(pluginFolderPath, fileName));

            MessageBox.Show("插件安装成功！");
            button1.Enabled = true;
            button2.Enabled = true;
            button2.Text = "安装";
        }

        private PluginList LoadLocalPluginList()
        {
            if (File.Exists(pluginJsonPath))
            {
                string json = File.ReadAllText(pluginJsonPath);
                return JsonConvert.DeserializeObject<PluginList>(json);
            }
            return new PluginList { List = new List<Plugin>() };
        }

        private void SaveLocalPluginList(PluginList pluginList)
        {
            string json = JsonConvert.SerializeObject(pluginList, Formatting.Indented);
            File.WriteAllText(pluginJsonPath, json);
        }

        private async Task DownloadFileAsync(string fileUrl, string destinationPath)
        {
            using (HttpClient client = new HttpClient())
            {
                byte[] fileBytes = await client.GetByteArrayAsync(fileUrl);
                await File.WriteAllBytesAsync(destinationPath, fileBytes);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }

    public class Author
    {
        public string Name { get; set; }
        public string Labels { get; set; }
        public string Img { get; set; }
    }

    public class File1
    {
        public string Type { get; set; }
        public string Url { get; set; }
    }

    public class Plugin
    {
        public string Name { get; set; }
        public string Info { get; set; }
        public string Version { get; set; }
        public string Date { get; set; }
        public Author Author { get; set; }
        public File1 File { get; set; }
    }

    public class PluginList
    {
        public List<Plugin> List { get; set; }
    }
}
