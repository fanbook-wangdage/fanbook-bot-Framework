using Newtonsoft.Json;

namespace Settings
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            this.StartPosition = FormStartPosition.CenterScreen;
            this.TopMost = true;
            InitializeComponent();
            this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);
            listBox1.SelectedIndex = 0;

            string filePath = @"Settigs.json";
            string json = File.ReadAllText(filePath);
            Person person = JsonConvert.DeserializeObject<Person>(json);
            textBox1.Text = person.on_start;
            checkBox1.Checked = person.on_end_restart;
            checkBox2.Checked = person.on_error_restart;

        }
        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex != -1)
            {
                // ��ȡ�û�ѡ�������
                string selectedItem = listBox1.SelectedItem.ToString();
                if (selectedItem == "��������")
                {
                    panel2.Visible = true;
                    panel1.Visible = false;
                }
                else
                {
                    panel2.Visible = false;
                    panel1.Visible = true;
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // ����һ������
            Person person = new Person
            {
                on_start = textBox1.Text,
                on_end_restart = checkBox1.Checked,
                on_error_restart = checkBox2.Checked
            };
            string json = JsonConvert.SerializeObject(person, Formatting.Indented);
            string filePath = @"Settigs.json";
            File.WriteAllText(filePath, json);
            MessageBox.Show("�����ѳɹ�����", "����ɹ�");
        }
    }
    // ����һ��������JSON���ݶ�Ӧ
    public class Person
    {
        public string on_start { get; set; }
        public bool on_end_restart { get; set; }
        public bool on_error_restart { get; set; }
    }
}
