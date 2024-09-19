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

            string filePath = @"Settings.json";
            try{
                string json2 = File.ReadAllText(filePath);
            }catch (FileNotFoundException)
            {
                // ����ļ������ڣ��򴴽�һ��Ĭ�ϵ������ļ�
                Person person1 = new Person
                {
                    on_start = "",
                    on_end_restart = false,
                    on_error_restart = false,
                    on_end_restart_time=5,
                    on_err_restart_time=5,
                    on_end_restart_log="�������",
                    on_end_restart_out_to_file=false,
                    on_errror_log=true
                };
                string json1 = JsonConvert.SerializeObject(person1, Formatting.Indented);
                File.WriteAllText(filePath, json1);
            
            }
            string json = File.ReadAllText(filePath);
            Person person = JsonConvert.DeserializeObject<Person>(json);
            textBox1.Text = person.on_start;
            checkBox1.Checked = person.on_end_restart;
            checkBox2.Checked = person.on_error_restart;
            numericUpDown1.Value = person.on_end_restart_time;
            textBox2.Text = person.on_end_restart_log;
            checkBox3.Checked = person.on_end_restart_out_to_file;

            numericUpDown2.Value = person.on_err_restart_time;
            checkBox4.Checked = person.on_errror_log;

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
                on_error_restart = checkBox2.Checked,
                on_end_restart_time = (int)numericUpDown1.Value,
                on_err_restart_time = (int)numericUpDown2.Value,
                on_end_restart_log = textBox2.Text,
                on_end_restart_out_to_file = checkBox3.Checked,
                on_errror_log = checkBox4.Checked

                
            };
            string json = JsonConvert.SerializeObject(person, Formatting.Indented);
            string filePath = @"Settings.json";
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
        public int on_end_restart_time { get; set; }
        public int on_err_restart_time { get; set; }
        public string on_end_restart_log { get; set; }
        public bool on_end_restart_out_to_file { get; set; }
        public bool on_errror_log { get; set; }
    }
}
