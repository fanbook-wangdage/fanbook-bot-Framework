using Newtonsoft.Json;

namespace pluginInstallTool
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.Load += Form1_Load;
            listBox1.SelectedIndex = -1;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;
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
            PluginList pluginList = JsonConvert.DeserializeObject<PluginList>(json);

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


    }
    public class Author
    {
        public string Name { get; set; }
        public string Labels { get; set; }
        public string Img { get; set; }
    }

    public class File
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
        public File File { get; set; }
    }

    public class PluginList
    {
        public List<Plugin> List { get; set; }
    }

}