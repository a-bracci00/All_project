public class Risorsa: IDisposable
{
// handle di una risorsa unmanaged, ad esempio di un file
    private IntPtr handle;
    // una Icon è una risorsa managed.
    private Icon icona;
    private bool disposed = false;
    public Risorsa(IntPtr handle,string iconfile)
    {
        this.handle = handle;
        this.icona=new Icon(iconfile);
    }
    // Implementazione di IDisposable.
    public void Dispose()
    {
        Console.WriteLine("Dispose()");
        Dispose(true);
    // Informa il CLR di non invocare il distruttore
    // perchè le risorse sono state liberate con il Dispose precedente
        GC.SuppressFinalize(this);
    }
    // se disposing è true, vengono liberate sia risorse Managed che unmanaged.
    // con disposing = false, il metodo viene richiamato internamente dal CLR,
    // esattamente dal distruttore, che avrà già liberato le risorse managed,
    // dunque qui vengono ripulite solo quelle unmanaged.
    private void Dispose(bool disposing)
    {
        Console.WriteLine("Dispose({0})",disposing);
        if(!this.disposed)
        {
        if(disposing)
        {
    // l'icona è una risorsa managed
        icona.Dispose();
    }
    // libera opportunamente le risorse unmanaged
        CloseHandle(handle);
        handle = IntPtr.Zero;
        }
    //per evitare che Dispose venga eseguito più volte
    disposed = true;
    }
    [System.Runtime.InteropServices.DllImport("Kernel32")]
    private extern static Boolean CloseHandle(IntPtr handle);
    // Il distruttore viene invocato automaticamente
    // e solo se non è stato invocato il metodo Dispose
    ~Risorsa()
    {
    Console.WriteLine("~Risorsa()");
    Dispose(false);
    }
}