using System;
using System.Windows;
using System.Windows.Input;
using System.Net.Http;

namespace BOE_Connect
{
  /// <summary>
  /// Interaction logic for MainWindow.xaml
  /// </summary>
  public partial class MainWindow : Window
  {
    public MainWindow()
    {
      InitializeComponent();
      // initalize http client
    }
    private void Button_Click(object sender, RoutedEventArgs e)
    {
      try
      {
        //show camera in webbrowser
        browser.Load("http://" + server_box.Text + ":" + camera_port.Text+"/video");

        //change connected to true
        Vars.connected = true;
      }
      catch (Exception)
      {
        MessageBox.Show("Unable to Connect to Server", "Unable to Connect to Server", MessageBoxButton.OK, MessageBoxImage.Error);
      }
    }

    //handle key down events
    private void OnKeyDownHandler(object sender, KeyEventArgs e)
    { if (Vars.connected)
      {
        if (e.Key == Key.W)
        {
          // send command
          sendCommand("wwwww");
        }
        if (e.Key == Key.S)
        {
          sendCommand("sssss");
        }
        if (e.Key == Key.D)
        {
          sendCommand("dd");
        }
        if (e.Key == Key.A)
        {
          sendCommand("aa");
        }
        if (e.Key == Key.K)
        {
          sendCommand("k");
        }
        if (e.Key == Key.L)
        {
          sendCommand("l");
        }
      }
    }

    private void sendCommand(string command)
    {
      try
      {
        Uri wsURL = new Uri("http://" + server_box.Text + ":" + webserver_port.Text + "/"+command);
        Vars.client.GetAsync(wsURL);
      }
      catch (Exception ex)
      {
        MessageBox.Show(ex.ToString());
      }
    }
  }

  public class Vars
  {
    public static HttpClient client = new HttpClient();
    public static bool connected = false;
  }
}
