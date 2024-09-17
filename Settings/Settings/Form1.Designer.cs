namespace Settings
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            listBox1 = new ListBox();
            label1 = new Label();
            button1 = new Button();
            button2 = new Button();
            panel1 = new Panel();
            textBox1 = new TextBox();
            label2 = new Label();
            panel2 = new Panel();
            checkBox4 = new CheckBox();
            checkBox3 = new CheckBox();
            label18 = new Label();
            textBox2 = new TextBox();
            label17 = new Label();
            label16 = new Label();
            label15 = new Label();
            label14 = new Label();
            numericUpDown2 = new NumericUpDown();
            label13 = new Label();
            numericUpDown1 = new NumericUpDown();
            label12 = new Label();
            label10 = new Label();
            checkBox2 = new CheckBox();
            label9 = new Label();
            label8 = new Label();
            label7 = new Label();
            label6 = new Label();
            label5 = new Label();
            label4 = new Label();
            checkBox1 = new CheckBox();
            label3 = new Label();
            label11 = new Label();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown2).BeginInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).BeginInit();
            SuspendLayout();
            // 
            // listBox1
            // 
            listBox1.BackColor = SystemColors.ControlLightLight;
            listBox1.BorderStyle = BorderStyle.FixedSingle;
            listBox1.Font = new Font("Microsoft YaHei UI", 10F, FontStyle.Bold);
            listBox1.FormattingEnabled = true;
            listBox1.HorizontalScrollbar = true;
            listBox1.ItemHeight = 19;
            listBox1.Items.AddRange(new object[] { "启动设置", "运行设置" });
            listBox1.Location = new Point(-1, -1);
            listBox1.Name = "listBox1";
            listBox1.Size = new Size(120, 325);
            listBox1.TabIndex = 0;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Microsoft YaHei UI", 10F, FontStyle.Bold);
            label1.Location = new Point(125, 9);
            label1.Name = "label1";
            label1.Size = new Size(79, 19);
            label1.TabIndex = 1;
            label1.Text = "配置编辑器";
            // 
            // button1
            // 
            button1.BackColor = SystemColors.ControlLightLight;
            button1.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button1.FlatAppearance.MouseDownBackColor = Color.Silver;
            button1.FlatAppearance.MouseOverBackColor = SystemColors.Control;
            button1.FlatStyle = FlatStyle.Flat;
            button1.Location = new Point(632, 290);
            button1.Name = "button1";
            button1.Size = new Size(75, 27);
            button1.TabIndex = 2;
            button1.Text = "退出";
            button1.UseVisualStyleBackColor = false;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.BackColor = SystemColors.ControlLightLight;
            button2.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button2.FlatAppearance.MouseDownBackColor = Color.Silver;
            button2.FlatAppearance.MouseOverBackColor = SystemColors.Control;
            button2.FlatStyle = FlatStyle.Flat;
            button2.Location = new Point(713, 290);
            button2.Name = "button2";
            button2.Size = new Size(75, 27);
            button2.TabIndex = 3;
            button2.Text = "保存";
            button2.UseVisualStyleBackColor = false;
            button2.Click += button2_Click;
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.ControlLightLight;
            panel1.BorderStyle = BorderStyle.FixedSingle;
            panel1.Controls.Add(textBox1);
            panel1.Controls.Add(label2);
            panel1.Location = new Point(125, 31);
            panel1.Name = "panel1";
            panel1.Size = new Size(663, 253);
            panel1.TabIndex = 4;
            panel1.Visible = false;
            // 
            // textBox1
            // 
            textBox1.BorderStyle = BorderStyle.FixedSingle;
            textBox1.Location = new Point(3, 20);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(578, 23);
            textBox1.TabIndex = 1;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(-1, 0);
            label2.Name = "label2";
            label2.Size = new Size(208, 17);
            label2.TabIndex = 0;
            label2.Text = "启动时自动运行(填路径，留空取消)：";
            // 
            // panel2
            // 
            panel2.AutoScroll = true;
            panel2.BackColor = SystemColors.ControlLightLight;
            panel2.BorderStyle = BorderStyle.FixedSingle;
            panel2.Controls.Add(checkBox4);
            panel2.Controls.Add(checkBox3);
            panel2.Controls.Add(label18);
            panel2.Controls.Add(textBox2);
            panel2.Controls.Add(label17);
            panel2.Controls.Add(label16);
            panel2.Controls.Add(label15);
            panel2.Controls.Add(label14);
            panel2.Controls.Add(numericUpDown2);
            panel2.Controls.Add(label13);
            panel2.Controls.Add(numericUpDown1);
            panel2.Controls.Add(label12);
            panel2.Controls.Add(label10);
            panel2.Controls.Add(checkBox2);
            panel2.Controls.Add(label9);
            panel2.Controls.Add(label8);
            panel2.Controls.Add(label7);
            panel2.Controls.Add(label6);
            panel2.Controls.Add(label5);
            panel2.Controls.Add(label4);
            panel2.Controls.Add(checkBox1);
            panel2.Controls.Add(label3);
            panel2.Location = new Point(125, 31);
            panel2.Name = "panel2";
            panel2.Size = new Size(663, 253);
            panel2.TabIndex = 2;
            // 
            // checkBox4
            // 
            checkBox4.AutoSize = true;
            checkBox4.Location = new Point(125, 230);
            checkBox4.Name = "checkBox4";
            checkBox4.Size = new Size(15, 14);
            checkBox4.TabIndex = 23;
            checkBox4.UseVisualStyleBackColor = true;
            // 
            // checkBox3
            // 
            checkBox3.AutoSize = true;
            checkBox3.Location = new Point(374, 92);
            checkBox3.Name = "checkBox3";
            checkBox3.Size = new Size(15, 14);
            checkBox3.TabIndex = 22;
            checkBox3.UseVisualStyleBackColor = true;
            // 
            // label18
            // 
            label18.AutoSize = true;
            label18.Location = new Point(329, 90);
            label18.Name = "label18";
            label18.Size = new Size(44, 17);
            label18.TabIndex = 21;
            label18.Text = "到日志";
            // 
            // textBox2
            // 
            textBox2.BorderStyle = BorderStyle.FixedSingle;
            textBox2.Location = new Point(101, 88);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(222, 23);
            textBox2.TabIndex = 20;
            // 
            // label17
            // 
            label17.AutoSize = true;
            label17.Location = new Point(3, 90);
            label17.Name = "label17";
            label17.Size = new Size(92, 17);
            label17.TabIndex = 19;
            label17.Text = "运行结束时记录";
            // 
            // label16
            // 
            label16.AutoSize = true;
            label16.Location = new Point(3, 228);
            label16.Name = "label16";
            label16.Size = new Size(116, 17);
            label16.TabIndex = 17;
            label16.Text = "发生异常时写入日志";
            // 
            // label15
            // 
            label15.AutoSize = true;
            label15.Location = new Point(182, 199);
            label15.Name = "label15";
            label15.Size = new Size(20, 17);
            label15.TabIndex = 16;
            label15.Text = "秒";
            // 
            // label14
            // 
            label14.AutoSize = true;
            label14.Location = new Point(191, 59);
            label14.Name = "label14";
            label14.Size = new Size(20, 17);
            label14.TabIndex = 15;
            label14.Text = "秒";
            // 
            // numericUpDown2
            // 
            numericUpDown2.BorderStyle = BorderStyle.FixedSingle;
            numericUpDown2.Location = new Point(56, 197);
            numericUpDown2.Name = "numericUpDown2";
            numericUpDown2.Size = new Size(120, 23);
            numericUpDown2.TabIndex = 14;
            numericUpDown2.Value = new decimal(new int[] { 5, 0, 0, 0 });
            // 
            // label13
            // 
            label13.AutoSize = true;
            label13.Location = new Point(3, 199);
            label13.Name = "label13";
            label13.Size = new Size(56, 17);
            label13.TabIndex = 13;
            label13.Text = "重启延时";
            // 
            // numericUpDown1
            // 
            numericUpDown1.BorderStyle = BorderStyle.FixedSingle;
            numericUpDown1.Location = new Point(65, 56);
            numericUpDown1.Name = "numericUpDown1";
            numericUpDown1.Size = new Size(120, 23);
            numericUpDown1.TabIndex = 12;
            numericUpDown1.Value = new decimal(new int[] { 5, 0, 0, 0 });
            // 
            // label12
            // 
            label12.AutoSize = true;
            label12.Location = new Point(3, 59);
            label12.Name = "label12";
            label12.Size = new Size(56, 17);
            label12.TabIndex = 10;
            label12.Text = "重启延时";
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.ForeColor = SystemColors.MenuHighlight;
            label10.Location = new Point(-4, 245);
            label10.Name = "label10";
            label10.Size = new Size(658, 17);
            label10.TabIndex = 9;
            label10.Text = "——————————————————————————————————————————————————\r\n";
            // 
            // checkBox2
            // 
            checkBox2.AutoSize = true;
            checkBox2.Location = new Point(149, 170);
            checkBox2.Name = "checkBox2";
            checkBox2.Size = new Size(15, 14);
            checkBox2.TabIndex = 8;
            checkBox2.UseVisualStyleBackColor = true;
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Location = new Point(3, 168);
            label9.Name = "label9";
            label9.Size = new Size(140, 17);
            label9.TabIndex = 7;
            label9.Text = "发生异常时自动重启程序";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.ForeColor = SystemColors.MenuHighlight;
            label8.Location = new Point(-4, 141);
            label8.Name = "label8";
            label8.Size = new Size(658, 17);
            label8.TabIndex = 6;
            label8.Text = "——————————————————————————————————————————————————\r\n";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label7.ForeColor = SystemColors.MenuHighlight;
            label7.Location = new Point(3, 124);
            label7.Name = "label7";
            label7.Size = new Size(56, 17);
            label7.TabIndex = 5;
            label7.Text = "异常捕获";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.ForeColor = SystemColors.MenuHighlight;
            label6.Location = new Point(-4, 107);
            label6.Name = "label6";
            label6.Size = new Size(658, 17);
            label6.TabIndex = 4;
            label6.Text = "——————————————————————————————————————————————————\r\n";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.ForeColor = SystemColors.MenuHighlight;
            label5.Location = new Point(-1, 16);
            label5.Name = "label5";
            label5.Size = new Size(658, 17);
            label5.TabIndex = 3;
            label5.Text = "——————————————————————————————————————————————————";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label4.ForeColor = SystemColors.MenuHighlight;
            label4.Location = new Point(3, 0);
            label4.Name = "label4";
            label4.Size = new Size(56, 17);
            label4.TabIndex = 2;
            label4.Text = "运行事件";
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(161, 36);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(15, 14);
            checkBox1.TabIndex = 1;
            checkBox1.UseVisualStyleBackColor = true;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(3, 33);
            label3.Name = "label3";
            label3.Size = new Size(152, 17);
            label3.TabIndex = 0;
            label3.Text = "运行结束以后自动重启程序";
            // 
            // label11
            // 
            label11.AutoSize = true;
            label11.Location = new Point(125, 300);
            label11.Name = "label11";
            label11.Size = new Size(25, 17);
            label11.TabIndex = 5;
            label11.Text = "1.1";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(800, 325);
            Controls.Add(label11);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label1);
            Controls.Add(listBox1);
            FormBorderStyle = FormBorderStyle.None;
            Name = "Form1";
            Text = "配置编辑器";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown2).EndInit();
            ((System.ComponentModel.ISupportInitialize)numericUpDown1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ListBox listBox1;
        private Label label1;
        private Button button1;
        private Button button2;
        private Panel panel1;
        private Label label2;
        private TextBox textBox1;
        private Panel panel2;
        private CheckBox checkBox1;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label7;
        private Label label6;
        private Label label10;
        private CheckBox checkBox2;
        private Label label9;
        private Label label8;
        private Label label11;
        private Label label12;
        private NumericUpDown numericUpDown1;
        private Label label15;
        private Label label14;
        private NumericUpDown numericUpDown2;
        private Label label13;
        private Label label16;
        private Label label17;
        private CheckBox checkBox3;
        private Label label18;
        private TextBox textBox2;
        private CheckBox checkBox4;
    }
}
