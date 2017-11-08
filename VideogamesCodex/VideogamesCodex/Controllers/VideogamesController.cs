using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using VideogamesCodex.Models;

namespace VideogamesCodex.Controllers
{
    public class VideogamesController : Controller
    {
        // GET: Videogames
        public ActionResult Index()
        {
            List<Videogames> videogames = Videogames.SelectAll();
            return View(videogames);
        }


        public ActionResult Ver(int id)
        {
            Videogames videogames = Videogames.GetVideogames(id);
            if (videogames != null)
            {
                return View(videogames);
            }
            else
            {
                return Redirect("~/");
            }

        }

        public ActionResult Modificar(int id = 0) //Modificar.cshtml
        {
            Videogames videogames = Videogames.GetVideogames(id);
            if (videogames == null)
            {
                return Redirect("~/Home/crear/");
            }
            else
            {
                return View("~/Views/Home/VideogamesForm.cshtml", videogames);
            }

        }
        public ActionResult Guardar(Videogames videogames)
        {
            //Guardar esos datos en db.
            videogames.Save();
            //Redireccionar a una vista.
            return Redirect("~/Home/Ver/" + videogames.id);
        }
        public ActionResult Eliminar(int id = 0)
        {
            //Eliminar la entrada si existe.
            Videogames videogames = Videogames.GetVideogames(id);
            if (videogames != null)
            {
                //Borrar
                videogames.Delete();
            }
            return Redirect("~/");
        }
    }
}