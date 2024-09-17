namespace pluginInstallTool
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            listBox1 = new ListBox();
            label1 = new Label();
            button1 = new Button();
            button2 = new Button();
            label2 = new Label();
            panel1 = new Panel();
            label5 = new Label();
            label13 = new Label();
            label12 = new Label();
            label11 = new Label();
            label10 = new Label();
            label9 = new Label();
            label8 = new Label();
            label7 = new Label();
            label6 = new Label();
            pictureBox1 = new PictureBox();
            label4 = new Label();
            label3 = new Label();
            label14 = new Label();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // listBox1
            // 
            listBox1.BorderStyle = BorderStyle.None;
            listBox1.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            listBox1.FormattingEnabled = true;
            listBox1.ItemHeight = 17;
            listBox1.Location = new Point(0, -3);
            listBox1.Name = "listBox1";
            listBox1.Size = new Size(135, 238);
            listBox1.TabIndex = 0;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(141, 191);
            label1.Name = "label1";
            label1.Size = new Size(152, 17);
            label1.TabIndex = 1;
            label1.Text = "在左侧选择一个插件来操作";
            // 
            // button1
            // 
            button1.BackColor = SystemColors.ControlLightLight;
            button1.FlatAppearance.BorderColor = SystemColors.MenuHighlight;
            button1.FlatAppearance.MouseDownBackColor = Color.Silver;
            button1.FlatAppearance.MouseOverBackColor = Color.FromArgb(224, 224, 224);
            button1.FlatStyle = FlatStyle.Flat;
            button1.Location = new Point(632, 200);
            button1.Name = "button1";
            button1.Size = new Size(75, 26);
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
            button2.FlatAppearance.MouseOverBackColor = Color.FromArgb(224, 224, 224);
            button2.FlatStyle = FlatStyle.Flat;
            button2.Location = new Point(713, 200);
            button2.Name = "button2";
            button2.Size = new Size(75, 26);
            button2.TabIndex = 3;
            button2.Text = "安装";
            button2.UseVisualStyleBackColor = false;
            button2.Click += button2_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Microsoft YaHei UI", 10F, FontStyle.Bold);
            label2.Location = new Point(141, 9);
            label2.Name = "label2";
            label2.Size = new Size(93, 19);
            label2.TabIndex = 4;
            label2.Text = "插件安装工具";
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.ControlLightLight;
            panel1.BorderStyle = BorderStyle.FixedSingle;
            panel1.Controls.Add(label5);
            panel1.Controls.Add(label13);
            panel1.Controls.Add(label12);
            panel1.Controls.Add(label11);
            panel1.Controls.Add(label10);
            panel1.Controls.Add(label9);
            panel1.Controls.Add(label8);
            panel1.Controls.Add(label7);
            panel1.Controls.Add(label6);
            panel1.Controls.Add(pictureBox1);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(label3);
            panel1.Location = new Point(141, 31);
            panel1.Name = "panel1";
            panel1.Size = new Size(647, 157);
            panel1.TabIndex = 5;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.BackColor = Color.SpringGreen;
            label5.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label5.ForeColor = SystemColors.WindowText;
            label5.Location = new Point(490, 12);
            label5.Name = "label5";
            label5.Size = new Size(44, 17);
            label5.TabIndex = 12;
            label5.Text = "已验证";
            // 
            // label13
            // 
            label13.AutoSize = true;
            label13.Location = new Point(42, 104);
            label13.Name = "label13";
            label13.Size = new Size(50, 17);
            label13.TabIndex = 11;
            label13.Text = "label13";
            // 
            // label12
            // 
            label12.AutoSize = true;
            label12.Location = new Point(4, 104);
            label12.Name = "label12";
            label12.Size = new Size(44, 17);
            label12.TabIndex = 10;
            label12.Text = "类型：";
            // 
            // label11
            // 
            label11.AutoSize = true;
            label11.Location = new Point(42, 138);
            label11.Name = "label11";
            label11.Size = new Size(50, 17);
            label11.TabIndex = 9;
            label11.Text = "label11";
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Location = new Point(4, 138);
            label10.Name = "label10";
            label10.Size = new Size(44, 17);
            label10.TabIndex = 8;
            label10.Text = "版本：";
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Location = new Point(63, 121);
            label9.Name = "label9";
            label9.Size = new Size(43, 17);
            label9.TabIndex = 7;
            label9.Text = "label9";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Location = new Point(4, 121);
            label8.Name = "label8";
            label8.Size = new Size(68, 17);
            label8.TabIndex = 6;
            label8.Text = "更新日期：";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.BackColor = SystemColors.Highlight;
            label7.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label7.ForeColor = SystemColors.ControlLightLight;
            label7.Location = new Point(540, 12);
            label7.Name = "label7";
            label7.Size = new Size(32, 17);
            label7.TabIndex = 5;
            label7.Text = "官方";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(360, 12);
            label6.Name = "label6";
            label6.Size = new Size(94, 17);
            label6.TabIndex = 4;
            label6.Text = "用户名(123456)";
            // 
            // pictureBox1
            // 
            pictureBox1.BorderStyle = BorderStyle.FixedSingle;
            pictureBox1.Image = (Image)resources.GetObject("pictureBox1.Image");
            pictureBox1.Location = new Point(323, 3);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(37, 37);
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.TabIndex = 2;
            pictureBox1.TabStop = false;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(4, 17);
            label4.Name = "label4";
            label4.Size = new Size(32, 17);
            label4.TabIndex = 1;
            label4.Text = "描述";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label3.Location = new Point(3, 0);
            label3.Name = "label3";
            label3.Size = new Size(44, 17);
            label3.TabIndex = 0;
            label3.Text = "插件名";
            // 
            // label14
            // 
            label14.AutoSize = true;
            label14.Location = new Point(141, 209);
            label14.Name = "label14";
            label14.Size = new Size(25, 17);
            label14.TabIndex = 6;
            label14.Text = "1.0";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(800, 229);
            Controls.Add(label14);
            Controls.Add(panel1);
            Controls.Add(label2);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label1);
            Controls.Add(listBox1);
            FormBorderStyle = FormBorderStyle.None;
            Name = "Form1";
            Text = "插件安装工具";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ListBox listBox1;
        private Label label1;
        private Button button1;
        private Button button2;
        private Label label2;
        private Panel panel1;
        private PictureBox pictureBox1;
        private Label label4;
        private Label label3;
        private Label label6;
        private Label label7;
        private Label label9;
        private Label label8;
        private Label label11;
        private Label label10;
        private Label label13;
        private Label label12;
        private Label label5;
        private Label label14;
    }
}
