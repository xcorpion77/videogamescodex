namespace VideogamesCodex.Models
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;
    using System.Linq;

    public partial class Videogames
    {
        public int id { get; set; }

        [Required]
        [StringLength(50)]
        public string name { get; set; }

        [Required]
        [StringLength(50)]
        public string publisher { get; set; }

        public int year { get; set; }

        private int genre { get; set; }
        public genre Genre
        {
            get
            {
                return (genre)genre;
            }
            set
            {
                if (genre > 0 && genre < 5)
                {
                    genre = (int)value;
                }
                else
                {
                    genre = 0;
                }
                
            }
        }
        private int platform { get; set; }
        public platform Platform
        {
            get
            {
                return (platform)platform;
            }
            set
            {
                if (platform > 0 && platform < 3)
                {
                    platform = (int)value;
                }
                else
                {
                    platform = 0;
                }
            }
        }

        private int score { get; set; }
        public score Score
        {
            get
            {
                return (score)score;
            }
            set
            {
                if (score > 00 && score < 100)
                {
                    score = (int)value;
                }
                else
                {
                    score = 0;
                }
            }
        }

        public bool online { get; set; }
        public online Online
        {
            get
            {
                return (online)((online) ? 1 : 0);
            }
            set
            {
                online = Convert.ToBoolean((int)value);
            }
        }

        public int pegi { get; set; }
        public pegi Pegi
        {
            get
            {
                return (pegi)pegi;
            }
            set
            {
                if (pegi > 0 && pegi < 4)
                {
                    pegi = (int)value;
                }
                else
                {
                    pegi = 0;
                }
            }
        }

        public static List<Videogames> SelectAll()
        {
            List<Videogames> videogames = new List<Videogames>();

            try
            {
                GameContext context = new GameContext();
                videogames = context.Videogames.ToList();
            }
            catch (Exception e)
            {
                throw;
            }
            return videogames;
        }

        public static Videogames GetVideogames(int id)
        {
            Videogames videogames = null;

            try
            {
                GameContext context = new GameContext();
                videogames = context.Videogames.SingleOrDefault();
            }
            catch (Exception e)
            {
                throw;
            }
            return videogames;
        }
        //Devuelve tarea o tareas donde el id sea ese o devuelte por defecto el primero que encuentra.


        public void Save()
        {
            bool create = this.id == 0;
            try
            {
                GameContext context = new GameContext();
                if (create)
                {
                    context.Entry(this).State = System.Data.Entity.EntityState.Added;
                }
                context.SaveChanges();
            }
            catch (Exception)
            {
                throw;
            }
        }

        public void Delete()
        {
            try
            {
                GameContext context = new GameContext();
                context.Entry(this).State = System.Data.Entity.EntityState.Deleted;
                context.SaveChanges();
            }
            catch (Exception)
            {
                throw;
            }
        }
    }
}
