namespace hj_update
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
            label1 = new Label();
            progressBar1 = new ProgressBar();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            button1 = new Button();
            button2 = new Button();
            label5 = new Label();
            label7 = new Label();
            label8 = new Label();
            label9 = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Microsoft YaHei UI", 15F, FontStyle.Bold);
            label1.ForeColor = SystemColors.Control;
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(328, 27);
            label1.TabIndex = 0;
            label1.Text = "王大哥Fanbook BOT环境更新工具";
            label1.Click += label1_Click;
            // 
            // progressBar1
            // 
            progressBar1.Location = new Point(12, 147);
            progressBar1.Name = "progressBar1";
            progressBar1.Size = new Size(762, 23);
            progressBar1.TabIndex = 1;
            progressBar1.Visible = false;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label2.ForeColor = SystemColors.Control;
            label2.Location = new Point(12, 54);
            label2.Name = "label2";
            label2.Size = new Size(104, 17);
            label2.TabIndex = 2;
            label2.Text = "你将更新主程序到";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label3.ForeColor = SystemColors.Control;
            label3.Location = new Point(116, 54);
            label3.Name = "label3";
            label3.Size = new Size(12, 17);
            label3.TabIndex = 3;
            label3.Text = " ";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label4.ForeColor = SystemColors.Control;
            label4.Location = new Point(138, 54);
            label4.Name = "label4";
            label4.Size = new Size(164, 17);
            label4.TabIndex = 4;
            label4.Text = "版本，点击安装按钮进行安装";
            // 
            // button1
            // 
            button1.FlatStyle = FlatStyle.Flat;
            button1.ForeColor = SystemColors.Control;
            button1.Location = new Point(699, 182);
            button1.Name = "button1";
            button1.Size = new Size(75, 25);
            button1.TabIndex = 5;
            button1.Text = "安装";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.FlatStyle = FlatStyle.Flat;
            button2.ForeColor = SystemColors.Control;
            button2.Location = new Point(618, 182);
            button2.Name = "button2";
            button2.Size = new Size(75, 25);
            button2.TabIndex = 6;
            button2.Text = "取消";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.ForeColor = SystemColors.Control;
            label5.Location = new Point(12, 193);
            label5.Name = "label5";
            label5.Size = new Size(25, 17);
            label5.TabIndex = 7;
            label5.Text = "1.0";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label7.ForeColor = SystemColors.Control;
            label7.Location = new Point(12, 80);
            label7.Name = "label7";
            label7.Size = new Size(68, 17);
            label7.TabIndex = 9;
            label7.Text = "本次更新：";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label8.ForeColor = SystemColors.Control;
            label8.Location = new Point(73, 80);
            label8.Name = "label8";
            label8.Size = new Size(12, 17);
            label8.TabIndex = 10;
            label8.Text = " ";
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Font = new Font("Microsoft YaHei UI", 9F, FontStyle.Bold);
            label9.ForeColor = SystemColors.Control;
            label9.Location = new Point(12, 127);
            label9.Name = "label9";
            label9.Size = new Size(0, 17);
            label9.TabIndex = 11;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Highlight;
            ClientSize = new Size(786, 219);
            Controls.Add(label9);
            Controls.Add(label8);
            Controls.Add(label7);
            Controls.Add(label5);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(progressBar1);
            Controls.Add(label1);
            FormBorderStyle = FormBorderStyle.None;
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private ProgressBar progressBar1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Button button1;
        private Button button2;
        private Label label5;
        private Label label7;
        private Label label8;
        private Label label9;
    }
}
